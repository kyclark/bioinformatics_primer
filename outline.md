# Practical Python for Bioinformatics/Data Science

This is a book written for the graduate student or post-doc who's expected to know how to process large amounts of data and generate reports and figures for papers but who has never been taught how to program. The author is a mostly self-trained programmer (though, aren't we all?), and this is the book that summarises what I've been doing in bioinformatics for the last 18 years or so.

# Chapter Summary

## Chapter 1: Unix intro

This chapters assumes no knowledge of the Unix command line, and so introduces common commands, the environment  (esp `$PATH`), directory structures, file permissions, man pages, etc. Many examples to show how to combine commands, introduction to languages like sed and awk. 

## Chapter 2: bash scripting

How to write bash commands to a file, make executable, run, place into `$PATH`, GNU parallel, shellcheck.

### Examples

1. Convert BAM files to FASTA/Q
2. Find unclustered proteins from CD-HIT

### Exercises

1. Download files with `wget`
2. `ls` for file sizes
3. `wc` for counting
4. ...

## Chapter 3: Make

How can we abuse GNU `make` to reproduce commands, make basic pipelines (unclustered proteins)?

### Examples

### Exercises

## Chapter 4: Python intro

How to create simple Python programs that take command-line arguments (lists).

### Examples

### Exercises

## Chapter 5: Strings, lists, tuples

How are strings, lists, and tuples similar (iteration).

### Examples

### Exercises

## Chapter 6: Dictionaries and sets

### Examples

### Exercises

## Chapter 7: Regular expressions

### Examples

1. Sequence type guesser
2. Dates
3. Latitude/longitude

### Exercises

## Chapter 8: Logging

### Examples

### Exercises

## Chapter 9: Testing

### Examples

### Exercises

## Chapter 10: Parsing delimited text

CSV and tab-delimited, blast -outfmt 6, GFF

### Examples

1. Find overlapping genes in yeast GFF
2. Parsing UProC output

### Exercises

## Chapter 11: Sequence formats 

FASTA, FASTQ, GenBank, SwissProt

### Examples

### Exercises

## Chapter 12: XML and JSON

NCBI taxonomy, web API calls

### Examples

1. Fetch PubMed JSON from API

### Exercises

## Chapter 13: Sequence similarity

Counting words, Hamming distance, character/kmer frequencies (machine learning), BLAST

### Examples

### Exercises

## Chapter 14: Graphs and ontologies

Graph theory, sequence assembly, ontologies e.g. Gene Ontology

### Examples

### Exercises

## Chapter 15: SQLite

### Examples

### Exercises

## Chapter 16: Pipelines

### Examples

### Exercises