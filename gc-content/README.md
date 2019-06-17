# Finding GC Content in Sequences

Write a Python program called `gc.py` that takes a single positional argument which should be a file. Die with a warning if the argument is not a file. For each line in the file, print the line number and the percentage of the characters on that line that are a "G" or "C" (case-insensitive).

````
$ ./gc.py
usage: gc.py [-h] FILE
gc.py: error: the following arguments are required: FILE
$ ./gc.py foo
"foo" is not a file
$ ./gc.py samples/sample1.txt
  1:   9%
  2:  19%
  3:  19%
  4:  22%
  5:  32%
  6:  21%
````
