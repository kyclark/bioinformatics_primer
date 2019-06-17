# Introduction: Bioinformatics Primer for bash and Python

This book is dedicated to the students and post-docs in science who've come from the bench and now need to learn how to use the command line. In my experience, few ever get any formal training in how to write software, so I want to give you as many examples as possible of complete, command-line programs that work, have documentation, and are testable and reproducible.

I got into bioinformatics by coming from the software industry and having to learn enough biology to write the code my bosses requested. I know well the feeling of being in over your head. Even after 24 years of programming, 18 in bioinformatics, I still sometimes feel completely lost in how to write a particular piece of code. In my experience, the best help for me is working examples of code that I can copy and paste into my programs, and so that's what I'm giving you.

## Organization

> "The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie

The best way to learn is by *doing*, so along with reading material about bash and Python, I will give you many programs that I want you to *write* in those languages. Each one will have a README that lays out the specifications ("specs") along with examples of how the program should work. Also included will be sample input files and a `test.py` program which you can run with the command `make test` (if you have `make` on your system) or `pytest -v test.py`.

I include my own version of a solution that you can use to compare. I spent many years in the Perl community where "There Is More Than One Way To Do It" (TIMTOWTDI) is something of a mantra whereas the Python community espouses "There should be one -- and preferably only one -- obvious way to do it" (https://www.python.org/dev/peps/pep-0020/). I disagree with this notion and believe you can find many creative and beautiful solutions. More than anything, the solution that you figured out, that you understand, and that satisfies the test suite is the "right" one for you. Your style will change as you grow more knowledgeable and confident in your programming skills.

### Shell

Most of bioinformatics happens on the Unix command line or "shell", so we need to start there. There are many terrific resources for learning from books to online courses like Coursera and the Software and Data Carpentries websites and workshops. I highly recommend you use all those to supplement the brief overview I will provide. 

### Shell Scripting

Shell scripts are commands written into a file and executed sequentially, top-to-bottom, so once you learn Unix commands, we can put those commands into files and run them later. This makes them documented and reproducible! 

### Make

We can further record commands and workflows by abusing GNU `make` and "makefiles." 

### Git

We use `git` to manage our source code.

### Python

Once you have an idea how to use Unix to manage files, permissions, and execute programs, we will start learning Python. 

### Appendices

Several topics are common to many or all the programs presented such as how to use `argparse` or regular expressions. I also provide two appendices showing small pieces of code in `bash` and Python that do some specific task like check if a file exists or read a file line-by-line. You should look over this section and piece together ideas to accomplish the tasks.

After completing this material, you should be able to:

* Write, test, and document programs in bash and Python
* Use the source code management system Git to version, share, and distribute code
* Use parallelization techniques and hardware (HPC) to run programs faster
* Package and distribute software to create reproducible workflows

## Getting the Source Code

To get the source code for the book, I recommend you go to https://github.com/kyclark/practical_python_for_data_science and click the "fork" button in the upper-right and then add this repo as an upstream source:

````
$ git clone <your_fork_of_the_repo> ppds
$ cd ppds
$ REPO=https://github.com/kyclark/practical_python_for_data_science.git
$ git remote add upstream $REPO
````

To get new content, use `git pull upstream master`. I write the exercises in such a way that you will create new content that should not conflict with content I make.

## Programming Environment

The material begins with the Unix command line. If you are working on Windows, I highly recommend you install Windows Subsystem for Linux and probably GitBash. If you are on an Apple computer, you have a full Unix system available through your Terminal app. The author uses a Mac with iTerm and vim editor to write, debug, and run programs. You may wish to use an editor like Sublime, TextWrangler, or Atom or an integrated develoment environment (IDE) like VSCode or PyCharm. However you choose to *write* code, this material assume you will *run* it from the command line. For many reasons, I have chosen not to use Jupyter Notebooks. Some chapters may include a Notebook, but I would prefer to have students write command-line programs and use a testing framework like PyTest to ensure that code runs correctly, top to bottom.

## Python

I personally prefer statically typed and "functional" languages like Rust, Elm, and Haskell, but I concede the dominance of dynamically typed languages such as Perl, Python, and Ruby. This material is intended to steer the student towards best practices when working in Python to avoid what I consider to be dangerous tendencies of the language. I will be using Python version 3. 

## Author

> "Computer programming has always been a self-taught, maverick occupation." - Ellen Ullman

> "Every great developer you know got there by solving problems they were unqualified to solve until they actually did it." - Patrick McKenzie

My name is Ken Youens-Clark (https://orcid.org/0000-0001-9961-144X), and I'm a Senior Scientific Programmer at the University of Arizona. While I have a Masters of Science in Biosystems Engineering, my undergraduate trianing was a BA in English Lit with a minor in music. As a kid, I had a RadioShack computer (probably a TRS-80, but I don't really remember) on which I wrote maybe two programs in BASIC. I never got into computing until after completing my bachelor's degree in 1995 when I started playing with computers and databases at my first job. The next year I landed a position where I learned Visual Basic on Windows 3.1, and that was when I actually got hooked on programming and problem solving. Since then, I've worked in several languages on various operating systems, and I've learned by doing -- always having to tackle problems I was never trained to solve. I spent the longest part of my career using Perl in a bioinformatics settting, but Python has definitely taken over the data processing and machine learning space, so that's what I'll cover.

## Acknowledgements

I would not be where I am professionally without a string of terrific bosses who took a chance and hired me, taught me, and let me move on, starting with Eric Thorsen who showed me Visual Basic, Mike Doll who taught me to double every time estimate, Steve Reppucci who honed my Perl and sysadmin skills, Dr. Lincoln Stein who introduced me to bioinformatics and created the "Programming for Biologists" at Cold Spring Harbor Laboratory, Dr. Doreen Ware who let me work on all kinds of terribly interesting problems, and Dr. Bonnie Hurwitz who allowed me to write and present novel materials to her metagenomics and bioinformatics classes. I also would like to thank the students who showed me how to improve my lectures and assignments. Most importantly, I would be nothing without the love and support of my wife and children.

## Copyright

All material copyright Ken Youens-Clark 2019.
