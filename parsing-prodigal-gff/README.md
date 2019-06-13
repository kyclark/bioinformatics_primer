# Parsing GFF

Two of the most common output files in bioinformatics, GFF (General Feature Format) and BLAST's tab/CSV files do not include headers, so it's up to you to merge in the headers.  Additionally, some of the lines may be comments (they start with `#` just like bash and Python), so you should skip those.  Further, the last field in GFF is basically a dumping ground for whatever else the data provider felt like putting there.  Usually it's a bunch of "key=value" pairs, but there's no guarantee.  Let's take a look at parsing the GFF output from Prodigal:
