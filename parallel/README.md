# Using GNU Parallel to Run Concurrent Processes

"GNU parallel is a shell tool for executing jobs in parallel using one or more computers." (https://www.gnu.org/software/parallel/). To imagine working in parallel, think about the construction of the First Transcontinental Railroad that linked the East and West coasts of America. The companies involved didn't start from one end and build it to the other. The track was built in independent sections that eventually connected as this was faster and more efficient. If you have a large job that can be broken into smaller tasks that can be run independently from each other, it's more efficient to use multiple processors possibly over many machines to run as many tasks concurrently than to run one big task.

Imagine you need to BLAST several million sequences. You could just run `blastn` on the file and wait a few days for it to finish. Alternatively, you could split the sequences into several files and distribute the BLAST commands to several machines each of which might finish in hours rather than days. At the end, you would need only to concatenate the BLAST hits to get the same answer you would have gotten from BLASTing all the sequences in one file. 

The advantage of using an HPCC (high performance computing cluster) is that you have access to several "nodes" (machines), each of which can have many "cores" (CPUs). You split up the sequences, then tell the HPC scheduler how many machines with what kind of memory requirements you need for how long, and it will schedule and run the jobs for you as machines become available. 

Unfortunately, not everyone working in bioinformatics has ready access to a HPC cluster. Still, it's possible that you could enjoy the benefits of parallel computing. It's likely that even your laptop has more than one CPU that could be used in parallel or maybe your lab or PI has a beefy server somewhere that has 12-24 processors. If you write all the commands you need to run into to a file, you can then use `parallel` to use execute those commands using as many CPUs as you desire. As jobs finish, `parallel` will launch more, always keeping all the cores busy, much like an HPC scheduler.

I tend to use `parallel` in most of my pipelines, even if they will run on an HPC. Jobs like BLAST aren't actually great to parallelize because BLAST will often require all the available memory on the node, but something like converting FASTQ files to FASTA format is perfect to farm out to multiple CPUs. 

## "Hello" Program

We'll start simple by pretending this "hello.sh" is something more interesting than it really is:

````
$ cat -n hello.sh
     1	#!/usr/bin/env bash
     2
     3	if [[ $# -lt 1 ]]; then
     4	    printf "Usage: %s NAME\n" $(basename $0)
     5	    exit 1
     6	fi
     7
     8	NAME=$1
     9
    10	if [[ $NAME == 'Lord Voldemort' ]]; then
    11	    echo "Upon advice of my counsel, I respectfully refuse to say that name."
    12	    exit 1
    13	fi
    14
    15	echo "Hello, $1!"
$ ./hello.sh
Usage: hello.sh NAME
$ ./hello.sh Jan
Hello, Jan!
$ ./hello.sh "Lord Voldemort"
Upon advice of my counsel, I respectfully refuse to say that name.
````

## Jobs File

We'll write a `jobs` file that will run this program with various names:

````
$ cat jobs
./hello.sh Bobby
./hello.sh "Lord Voldemort"
./hello.sh Jan
./hello.sh Greg
./hello.sh Marcia
````


In a `Makefile`, I've documented several ways we could run this. 

````
$ cat Makefile
.PHONY: shell parallel halt

JOBS = 'jobs'

shell:
	bash $(JOBS)

parallel:
	parallel -j 2 < $(JOBS)

halt:
	parallel -j 2 --halt soon,fail=1 < $(JOBS)
````

## Running Jobs with bash

The simplest way to execute all the jobs is to tell `bash` to execute the lines in the `jobs` file:

````
$ make shell
bash 'jobs'
Hello, Bobby!
Upon advice of my counsel, I respectfully refuse to say that name.
Hello, Jan!
Hello, Greg!
Hello, Marcia!
````
## Running Jobs with parallel

Another option is to push the commands to `parallel` with an option `-j` to indicate how many CPUs to use concurrently. If you indicate more CPUs than you actually have, `parallel` will just use however many are available. If you don't tell `parallel` how many to use, it will use *all available CPUs* which is probably not what you want. It's often wise to leave 1 or 2 cores open for the machine itself! If we run `make parallel` to execute the `parallel` target, we see this:

````
$ make parallel
parallel -j 2 < 'jobs'
Hello, Bobby!
Upon advice of my counsel, I respectfully refuse to say that name.
Hello, Jan!
Hello, Greg!
Hello, Marcia!
make: *** [parallel] Error 1
````

One of the jobs failed. Sometimes you want everything to stop if you encounter a problem, e.g., one of your FASTA files was corrupted so you really need to fix it before finishing the rest of the analysis with incomplete data. You can tell `parallel` to "halt" when it encounters an error. See the `halt` target:

````
$ make halt
parallel -j 2 --halt soon,fail=1 < 'jobs'
Hello, Bobby!
Upon advice of my counsel, I respectfully refuse to say that name.
parallel: This job failed:
./hello.sh "Lord Voldemort"
parallel: Starting no more jobs. Waiting for 1 jobs to finish.
Hello, Jan!
make: *** [halt] Error 1
````

You see that we didn't get to the end of the jobs file. It happended that "Jan" was greeted after the error, but no other jobs were started because we told `parallel` to halt as soon as possible after encountering any error.

## Dynamically Writing a Jobs File

It's not typical that you would manually write a jobs file. Usually you have some input files or directories from the user and need to go find all the files to process. Here is an example of reading the top 100 boys' names from 1945 birth records and sending those to our `hello.sh` program.

````
$ cat -n run_names.sh
     1	#!/usr/bin/env bash
     2
     3	set -u
     4
     5	HELLO=${1:-"./hello.sh"}
     6	NAMES="../../../inputs/1945-boys.txt"
     7
     8	if [[ ! -f "$NAMES" ]]; then
     9	    echo "Missing NAMES \"$NAMES\""
    10	    exit 1
    11	fi
    12
    13	JOBS=$(mktemp)
    14	i=0
    15	while read -r NAME; do
    16	    i=$((i+1))
    17	    echo "$HELLO \"#$i $NAME\"" >> "$JOBS"
    18	done < "$NAMES"
    19
    20	parallel < "$JOBS"
    21
    22	rm "$JOBS"
    23	echo "Done."
````

Notice that I include the rank of each name. If the jobs file were run by `bash`, you would see them printed in order from 1 to 100. Since we ask `parallel` to run it, you'll most likely see them out of order:

````
$ ./run_names.sh | tail
Hello, #94 Herbert!
Hello, #95 Victor!
Hello, #96 Gregory!
Hello, #97 Curtis!
Hello, #98 Bernard!
Hello, #99 Clifford!
Hello, #67 Ronnie!
Hello, #1 James!
Hello, #100 Gene!
Done.
````

Our `hello.sh` is trivial and runs too quickly for us to really see the benenfits of CPU usage. Here is an equally trival program that runs much more slowly:

````
$ cat long_hello.sh
#!/usr/bin/env bash

[[ $# -eq 1 ]] && sleep 3 && echo "Hello, $1!"
````

If there is an argument, the program waits (`sleep`) for 3 seconds and then greets the argument. Run it like the other and see how long it takes:

````
$ ./long_hello.sh Frank
Hello, Frank!
````

Now use this program with the `run_names.sh` program:

````
$ ./run_names.sh ./long_hello.sh
````

Then use a program like `top` or `htop` on your system to watch how the CPUs are being used!

## Summary

To paraphrase Dr. Ian Malcolm, just because you *can* parallelize jobs doesn't mean you always *should* do so. As stated before, jobs that use loads of memory like BLAST probably should not be unless more than one copy of the database can fit into memory. Jobs that are mostly I/O (input/output) are good candidates for use with `parallel`. 