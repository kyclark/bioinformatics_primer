# Parsing Putative Genes in Prodigal GFF

Two of the most common output files in bioinformatics, GFF (General Feature Format) and BLAST's tab/CSV files *do not include headers*, so it's up to you to merge in the headers.  Additionally, some of the lines may be comments (they start with `#` just like bash and Python) or may be blank, so you should skip those.  Further, the last field in GFF is basically a dumping ground for whatever metadata the author felt like putting there.  Usually it's a bunch of "key=value" pairs, but there's no guarantee.  

In our example, we have run the Prodigal gene predictor on a sample and wish to find putative genes with a minimum score. Prodigal can create output in either GenBank or GFF format, but the information contained is the same. Cf:

https://github.com/hyattpd/Prodigal/wiki/Understanding-the-Prodigal-Output

## GFF Structure

Take a look at the GFF output from Prodigal in `HUMANGUT_SMPL_INB.fa.prodigal.gff`. The first line is:

````
##gff-version  3
````

The double `##` means the line is not just a comment but a "directive" or a "pragma" and says this file follows the conventions of GFF version 3 which can be found at https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md.

According to the specifications, the columns are:

1. seqid
2. source
3. type
4. start
5. end
6. score
7. strand
8. phase
9. attributes

The ninth column reserves the following fields:

* ID
* Name
* Alias
* Parent
* Target
* Gap
* Derives_from
* Note
* Dbxref
* Ontology_term
* Is_circular

The second line is rather long and looks basically like this:

````
# Sequence Data: seqnum=1;seqlen=4867;
seqhdr="HumanGut_CONTIG_00235296 
/accession=HumanGut_CONTIG_00235296 
/length=4867 /length=4867 
/sample_id=1340106823570556171 
/sample_acc=HUMANGUT_SMPL_INB 
/sample_name=HUMANGUT_SMPL_INB 
/site_id_n=HUMANGUT_SITE_INB"
````

This is metadata provided by Prodigal about the subject file. You can see there are a couple of levels of *key=value* pairs. First in the pairs separated by `;` (`seqnum`, `seqlen`, and `seqhdr`), and then `seqhdr` contains additional *key=value* pairs separated by spaces and starting with a `/`.

The third line is also long and provides metadata about the model Prodigal used in the analysis:

````
# Model Data: version=Prodigal.v2.6.3;
run_type=Single;model="Ab initio";gc_cont=54.91;transl_table=11;uses_sd=0
````

Finally on line 4 the actual data starts. We can inspect it with a bit of command-line fu:

````
$ awk 'NR==4' HUMANGUT_SMPL_INB.fa.prodigal.gff | tabchk.py -N -
// ****** Record 1 ****** //
Field1 : HumanGut_CONTIG_00235296
Field2 : Prodigal_v2.6.3
Field3 : CDS
Field4 : 17
Field5 : 157
Field6 : 3.3
Field7 : +
Field8 : 0
Field9 : ID=1_1;partial=00;start_type=GTG;rbs_motif=None;\
rbs_spacer=None;gc_cont=0.688;conf=68.33;score=3.35;cscore=11.92;\
sscore=-8.57;rscore=-4.31;uscore=-1.25;tscore=-3.01;
````

It's not helpful to see "Field1" and such, so let's add in the field names:

````
$ awk 'NR==4' HUMANGUT_SMPL_INB.fa.prodigal.gff | \
> tabchk.py -f seqid,source,type,start,end,score,strand,frame,attributes -
// ****** Record 1 ****** //
seqid      : HumanGut_CONTIG_00235296
source     : Prodigal_v2.6.3
type       : CDS
start      : 17
end        : 157
score      : 3.3
strand     : +
frame      : 0
attributes : ID=1_1;partial=00;start_type=GTG;rbs_motif=None;rbs_spacer=None;\
             gc_cont=0.688;conf=68.33;score=3.35;cscore=11.92;sscore=-8.57;\
			 rscore=-4.31;uscore=-1.25;tscore=-3.01;
````

Now we'd like to find all the CDS records that had a `score` greater than some threshold. For that, we're going to need to check the `type` field and then find the `score` hidden in the `attributes` field. 

Just to be sure, what are the values for the `type` field?

````
$ awk -F"\t" 'NR>4 {print ($3==""?"NA":$3)}' \
> HUMANGUT_SMPL_INB.fa.prodigal.gff | sort | uniq -c
 356 CDS
 148 NA
````

## Parsing GFF with csv.DictReader

BioPython does not yet include a GFF parser, so we'll just handle it ourselves. Besides, there's so much we can learn! As stated before, there may be some comment lines that start with `#` that we need to skip, and the data lines are 9 tab-delimited fields for which we have names. All of this can be succinctly described to the `csv.DictReader` like so:

````
flds = 'seqid source type start end score strand frame attributes'.split()
reader = csv.DictReader(filter(lambda line: line[0] != '#', fh),
                        fieldnames=flds,
                        delimiter='\t')
````

The first argument to `csv.DictReader` should be a "stream" -- something that will produce the next line of input. An open file handle is usually what we pass, but it's also possible to use, say `io.StringIO` to make a string behave like a file handle. Here we are creating a `filter` object that will only allow lines from the `fh` that do not begin with `#`. We can also pass a list of `fieldnames`, and that the `delimiter` is a Tab character (`\t`). 

We could write a *generator* function that would `yield` each line of the file like so:

````
def src():
    for line in fh:
        if line[0] != '#':
            yield line

reader = csv.DictReader(src(), fieldnames=flds, delimiter='\t')
````

If you have more complex logic than will comfortably fit into a `filter`, it might be better to write it like this.

## Iterating GFF Records

With our handy CSV `reader`, we can do `for rec in reader` to iterate over a sequence of dictionaries that look like this:

````
OrderedDict([('seqid', 'HumanGut_CONTIG_00235296'),
             ('source', 'Prodigal_v2.6.3'),
             ('type', 'CDS'),
             ('start', '17'),
             ('end', '157'),
             ('score', '3.3'),
             ('strand', '+'),
             ('frame', '0'),
             ('attributes',
              'ID=1_1;partial=00;start_type=GTG;<...elided...>')])
````

I cut down the `attributes` for the moment. Since we only want "CDS" records, we `continue` (skip to the next iteration of the loop) `if rec['type'] != 'CDS'`. 

## Parsing GFF Attributes

The `rec['attributes']` are separated by the semi-colon `;`, so we can use that to `split` the string:

````
>>> attrs = 'ID=1_1;partial=00;start_type=GTG;rbs_motif=None;score=3.35'
>>> attrs.split(';')
['ID=1_1', 'partial=00', 'start_type=GTG', 'rbs_motif=None', 'score=3.35']
````

As it happens, they all have the structure "key=value", so we could `split` each of those on the equal sign `=`, but it's far safer to use a regular expression to validate that we have something that *really* looks like a key and value. This will make the script far more flexible and reusable!

````
>>> import re
>>> kv = re.compile('([^=]+)=([^=]+)')
>>> match = kv.match('partial=00')
>>> match
<re.Match object; span=(0, 10), match='partial=00'>
>>> match.groups()
('partial', '00')
````

When the `match` fails, it returns `None`, so it's important that we check that each attribute actually matched the regex. I chose to `map` each of the attributes into the regex. Note that here I introduce a fake attribute that won't match so you can see the `None`:

````
>>> attrs = 'ID=1_1;partial=00;start_type=GTG;rbs_motif=None;score=3.35;ABC'
>>> from pprint import pprint as pp
>>> pp(list(map(kv.match, attrs.split(';'))))
[<re.Match object; span=(0, 6), match='ID=1_1'>,
 <re.Match object; span=(0, 10), match='partial=00'>,
 <re.Match object; span=(0, 14), match='start_type=GTG'>,
 <re.Match object; span=(0, 14), match='rbs_motif=None'>,
 <re.Match object; span=(0, 10), match='score=3.35'>,
 None]
````

 
If there is a `match`, I use the `groups` method to unpack the two capturing groups into `key, value` so I can set my `attr` dictionary to those.
 
## Printing Wanted Values
 
Lastly we need to see if there is a `score` attribute by asking if that string exists in the keys of the `attrs` dictionary. If it does, we `try` to convert the value to a `float`. The `str` class has a very handy `isnumeric` method that can tell us if a string looks like an integer but it doesn't work with a float:

````
>>> '1'.isnumeric()
True
>>> '1.2'.isnumeric()
False
````

We could write a regular expression to check if a string looks like a floating point number, but there are really quite a lot of ways to represent a float, so it's easier to just see if Python is able to make the conversion. If we fall into the `except` branch, we just `pass` on to the next record. Only if we can make the conversion of `score` to a float and if that value is greather than or equal to the given `min_score` do we print out the sequence ID and the `score`.