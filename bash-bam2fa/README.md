# Bash: Convert BAM to FASTA (bam2fa)

Building on the `parallel` chapter, here is an example of a `bash` program that will convert BAM files to FASTA. SAM and BAM are formats for storing sequence alignments and stand for "Sequence Alignment Map" which is plain text and "Binary Alignment Map" which is the same information but stored in a compressed format only readable by machines. 

https://en.wikipedia.org/wiki/SAM_(file_format)

It's common to get SAM/BAM formats from a sequencing core as your sequences are often aligned to some reference like human. You can use `samtools` to look at the files and convert them to other formats easily enough. This program is designed to quickly convert a directory of BAM files into FASTA files that will live in some new directory.

## Checking and unpacking arguments

After using `set -u` to catch basic mistakes, we check `$#` to see how many arguments we have (mnemonic: `#` is the symbol for "number"). We need at least one argument but no more than 3. Print a usage if needed. Then we put `$1`, `$2`, etc. into judiciously named variables that describe what they are. Too often I see programs where `$1` is used throughout; while valid, this makes the code unreadable whereas `$INPUT` reminds me what the variable is supposed to be.

## Finding input files

The program is written so that it can either take the name of a file or a directory of files. I create temporary file `$FILES` to hold the input filenames. The `-f $INPUT` will be "True" if the argument is a file, so we `echo` the input value into the tempfile. If `-d $IN_DIR` is "True," then it names a directory that exists and so we `find` in there anything with a `-name` ending in `.bam` with a `-size` greater that `0` characters/bytes and send the output of that command into `$FILES`. If neither of these are true, we report an error and `exit 1`. 

## Temporary files

I prefer to use `mktemp` to get a temporary file. You could just overwrite a statically named `files.txt` file if you want, but you run the risk of accidentally overwriting a file that is still being used by another process. It's much safer to use `mktemp` as it guarantees a uniquely named file in a temporary directory. Additionally, if you forget to `rm` the file when you are done, it will likely be created in a location where old, unused files are regularly removed by the system.

## Exit codes

It's very important to `exit` with a *non-zero exit code* when there is an error. If you are using `make` or `parallel` or other programs to chain this, you can ensure the chain will fail if a component fails. *This is wise and good.* You do not want to complete an analysis pipeline if some key step fails. You want to report errors and halt processing until the error is fixed!

## Counting inputs

Since I've put all the input file names into a file, we need to count how many files there are which is what `wc -l` tells us. We need to do a bit of acrobatics to ensure we get only the number and not the name of the file, too:

````
$ wc -l bam2fa.sh
      67 bam2fa.sh
$ wc -l bam2fa.sh | awk '{print $1}'
67
````

With that, we can ask `bash` to coerce the string value into a number and see if it is less than 1 (`$NUM -lt 1`). If so, we exit with an error message and a non-zero `exit` value.

## Making output directory

We test if `! -d $OUT_DIR` to ask if this directory *does not* exist. If so, we create it with `mkdir -p` where the `-p` option tells `mkdir` to create "parent" directories as needed. That is, if the user wanted the output files to go into `$HOME/projects/foo/bar/fasta`, `mkdir` would fail if all the parent directories up to `fasta` if they didn't already exist. Without `-p`, `mkdir` would fail if any of the parent directories were not present.

## Create jobs file

I make a second temp file for the commands that need to be run, one for each file. I use `while read` to read each line from the `$FILES` into a variable called `BAM` that is the name of the BAM file. I like to print out "1: foo.bam", "2: bar.bam", etc., while processing so I can see what is happening and how many files are being processed, so I increment a counter `$i` by one and use `printf` to print out the counter as three-characters-wide digit (`%3d`), followed by a colon (`:`), followed by a string (`%s`) where I'll show the `basename` of the file where:

````
$ basename foo/bar/baz.bam
baz.bam
````

I want to use the basename of the file as the new filename but with the `.bam` extension removed which I can note as the optional second argument to `basename`:

````
$ basename foo/bar/baz.bam ".bam"
baz
````

I create the name of the new `FASTA` file by creating a new string `$OUT_DIR/$BASE.fa`. I use the test `! -f` to check if the file *does not exist*; if so, I `echo` the `samtools` command to convert it to `fasta` format, redirecting with the single `>` to put the output from `samtools` into the new `$FASTA` file. This whole command gets *appended* with the double `>>` into the `$JOBS` file. (I've have used a single `>` in that instance more times than I care to admit, which means that I will only run the last job because the single `>` *overwrites* any existing content!)

## Running the jobs file

I look for the `parallel` command using `which` to inspect my `$PATH` for any program with this name. If you have installed `parallel` on your system but this fails, it's probably because `parallel` exists in some location that is not in your `$PATH`. You can fix this by putting `parallel` into one of the directories in your `$PATH` or by appending the directory location into your existing `$PATH`. You could modify this script like so:

````
PATH=/directory/with/parallel:$PATH
````

Be sure it's the *directory* where `parallel` lives, not the path to the `parallel` program itself.

The `-z` test checks if a string is null which will be the case if `parallel` is not found. In that case, we execute all the commands with `sh`; otherwise, we run `parallel` with some number of cores, noting that any failures should `halt` the process.

## Cleaning up

Finally we remove (`rm`) our temporary files and say good-bye to the user. I always `echo "Done."` at the end of my `bash` programs just so I can see that I made it to the end of the program.

## Summary

This program shows you how to find input files, create an output directory, use temporary files, process input files with some program, and run those processes either serially or in parallel. This program weighs in at just over 60 lines, which is about the maximum number I feel comfortable writing in `bash`. It's a capable program, but if I wanted it to do much more, I'd be more comfortable writing it in Python.
