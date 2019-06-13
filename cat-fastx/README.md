# Concatenate FASTX Files

Given a directory/list of FASTQ/A files like this:

    1.SRR170176.fastq
    2.SRR170506.fastq
    3.SRR170739.fastq
    4.SRR328519.fastq
    5.SRR047943.fastq
    6.SRR048028.fastq

Concatenate all the sequences into one file. If a header looks like this:

    @GPSBU5C02GK9PQ

Turn it into this:

    @1.SRR170176_GPSBU5C02GK9PQ

