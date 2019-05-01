# BLAST pipeline

Edit the Makefile to indicate the input/output/blast directories, then type
"make"

```
$ make
find . \( -name \*.conf -o -name \*.OU \) -exec rm {} \;
./00-controller.sh -b /rsgrps/bhurwitz/hurwitzlab/data/reference/patric_bacteria/1313.2945.fna -f /rsgrps/bhurwitz/kyclark/human-gut/fasta -o /rsgrps/bhurwitz/kyclark/human-gut
  1: 01-fasta-split.sh [99204]
  2: 02-blast.sh [99205]
Done.
[hpc:service1@/rsgrps/bhurwitz/kyclark/abe487/book/hpc/pbs/blast]$ qs

service0:
                                                            Req'd  Req'd   Elap
Job ID          Username Queue    Jobname    SessID NDS TSK Memory Time  S Time
--------------- -------- -------- ---------- ------ --- --- ------ ----- - -----
99204.service1  kyclark  clu_stan 01-fasta-s    --    1   2    4gb 24:00 Q   --
99205.service1  kyclark  clu_stan 02-blast      --    1   2    4gb 24:00 H   --
```

The second job should start after the first one completes.
