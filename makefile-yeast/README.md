# Using a Makefile to Create Reproducible Workflows

GNU `make` is a program we can abuse to help create documented, reproducible workflows. It's intended purpose is to create executable files from source code for languages like `c` or `c++`. This process of turning text into machine instructions is called "compiling" and is often a long and tedious process. If a source code file has not changed since the last time the program was compile, `make` will not bother compiling it again. The compiler needs to compile some files before others and then go through a complicated graph of actions to make the executable. This is a workflow, and we can create our own `Makefile` that runs shell commands rather than compiling programs. It's not how `make` was intended to be used, but it works and you'd be surprised at just how far you can go with `make` before you need to investigate more complicated solutions like `snakemake` (which is `make` mixed with Python), Pegasus, Taverna, and the more than 100 other workflow management systems.

If you type `make` on the command line, it will look for a file called `Makefile` (or `makefile`) for instructions. If you look at the `Makefile.orig`, you will see that all the targets for this have been defined. 

````
$ head Makefile.orig
.PHONY: all fasta features test clean

all: clean fasta genome chr-count chr-size features gene-count verified-genes uncharacterized-genes gene-types terminated-genes

clean:
	find . \( -name \*gene\* -o -name chr-\* \) -exec rm {} \;

fasta:
	echo "Download files into \"fasta\" directory"
````

## Make Targets

A "target" in a Makefile is a word starting a line followed by a colon `:` and possibly a number of commands which are all indented by a *tab* character (spaces are not allowed). If you wanted to run the `fasta` target in the file above, you'd type `make fasta` and the `echo` command would be run.

If you find yourself running the same commands over and over, especially if you are scrolling up through your command history to find various encantations, you should consider creating a `Makefile` with targets, e.g., for each of the various data sets you are running.

## Automating Yeast Analysis

To start this exercise, copy this to start your `Makefile`:

````
$ cp Makefile.orig Makefile
$ git add Makefile
````

Your job is to figure out the correct Unix commands (or scripts) to create the correct content.
 
Add your Makefile and any other needed files (e.g., scripts) to your Git repo.  DO NOT ADD ANYTHING ELSE (e.g., the FASTA files)!!!
 
You may notice that there is a `.gitignore` file in there that lists files that Git should ... well, ignore. This is a great way to ensure you do not accidentally add files to Git that should not be there!

````
$ cat Makefile
.PHONY: all fasta features test clean

all: clean fasta genome chr-count chr-size features gene-count verified-genes uncharacterized-genes gene-types terminated-genes

clean:
	find . \( -name \*gene\* -o -name chr-\* \) -exec rm {} \;

fasta:
	echo "Download files into \"fasta\" directory"

genome: fasta
	echo OK > fasta/genome.fa

chr-count: genome
	echo OK > chr-count

chr-size: genome
	echo OK > chr-size

features:
	echo "Download SGD_features.tab"

gene-count: features
	echo OK > gene-count

verified-genes: features
	echo OK > verified-genes

uncharacterized-genes: features
	echo OK > uncharacterized-genes

gene-types: features
	echo OK > gene-types

palinsreg:
    echo "Unzipping palinsreg"

terminated-genes: palinsreg
    echo OK > terminated-genes

test:
	pytest -v test.py
````

## Targets

### 'fasta' target:
 
Download all the '.fsa' files (chr 1-16, mt) from http://downloads.yeastgenome.org/sequence/S288C_reference/chromosomes/fasta/  into a 'fasta' directory.
 
HINT: You can right-click on the links to copy the link location and then 'wget' the file.

### "genome" target:
 
Make a single whole genome file called `fasta/genome.fa`

### "chr-count" target:
 
Count the chromosomes in the whole genome file.  Put the number into a file called `chr-count`.
 
HINT: Each of the original FASTA files contains a single chromosome.

### "chr-size" target:
 
Find size of total genome.  Put the answer into a file called `chr-size`.
 
HINT: Look up the command `wc` and find out what it does. The size of the genome can be determined by counting the number of characters in the genome (not on the same line as a fasta header).

### "features" target:
 
Download the list of cerevisiae chromosome features: http://downloads.yeastgenome.org/curation/chromosomal_feature/SGD_features.tab
 
Columns:

* Primary Standfor Gene Database ID (SGDID) (mandatory)
* Feature type (mandatory)
* Feature qualifier (optional)
* Feature name (optional)
* Standard gene name (optional)
* Alias (optional, multiples separated by |)
* Parent feature name (optional)
* Secondary SGDID (optional, multiples separated by |)
* Chromosome (optional)1
* Start_coordinate (optional)1
* Stop_coordinate (optional)1
* Strand (optional)1
* Genetic position (optional)
* Coordinate version (optional)
* Sequence version (optional)
* Description (optional)

### 'gene-count' target:
 
Count total genes ('ORF's) from `SGD_features.tab` into a file called `gene-count`.

### 'verified-genes' target:
 
Count only verified genes from `SGD_features.tab` into a file called `verified-genes`.

### 'uncharacterized-genes' target:
 
Count only uncharacterized genesfrom `SGD_features.tab` into a file called `uncharacterized-genes`.

### 'gene-types' target:
 
Create file called `gene-types` that contains the counts of all the types of genes.

### 'palinsreg.txt'

The file `palinsreg.txt` has been provided for you in a zipped format. Unzip it.
 
These are detected terminator sequences in the E. coli genome (using the program GeSTer, if you're curious).
The command grep '/G=[^ ]*' somefile will find all lines that match /G=somegenename, where somegenename is a sequence of non-blank characters. Read the output of man grep and figure out how to -only print /G=somegenename, rather than the whole line.
Pipe the results of part (2) through a cut command to get only everything after the '='
Store the unique, sorted results of part (3) into a file named 'terminated-genes'


