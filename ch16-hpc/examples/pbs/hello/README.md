# Hello

Type "make" to submit the "hello.sh" job.  

```
$ make
qsub hello.sh
813113.service0
```

Then type "qstat" to see the progress of your job.  

```
service0:
                                                            Req'd  Req'd   Elap
Job ID          Username Queue    Jobname    SessID NDS TSK Memory Time  S Time
--------------- -------- -------- ---------- ------ --- --- ------ ----- - -----
813113.service0 kyclark  clu_stan hello.sh      --    1   2    4gb 01:00 Q   --
```


When finished, you should see out and error files (and hopefully the error 
file is empty).

```
$ ls -lh
total 128K
-rw-rw-r-- 1 kyclark staff    210 Aug 25 10:24 hello.sh
-rw------- 1 kyclark bhurwitz   0 Aug 25 10:25 hello.sh.e813113
-rw------- 1 kyclark bhurwitz 161 Aug 25 10:25 hello.sh.o813113
-rw-rw-r-- 1 kyclark staff     56 Aug 25 10:25 Makefile
-rw-rw-r-- 1 kyclark staff    428 Aug 25 10:23 README.md
$ cat hello.sh.o813113
Hello from sunny "r1i3n15"!
Your group bhurwitz has been charged 00:00:00 for 2 cpus.
You previously had 0.  You now have 0 remaining for the queue clu_standard
```

Type "make clean" to get rid of the HPC output.  Note that each submit will
automatically run "clean."  Alter the Makefile if you don't want that.
