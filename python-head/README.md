# File Handling: Emulate "head"

Create a Python program called `head.py` that expects one or two arguments. If there are no arguments, print a "Usage" statement. The first argument is required and much be a regular file; if it is not, print "<arg> is not a file" and exit *with an error code*. The second argument is optional. If given, it must be a positive number (non-zero); if it is not, then print "lines (<arg>) must be a positive number". If no argument is provided, use a default value of 3. You can expect that the test will only give you a value that can be safely converted to a number using the `int` function. If given good input, it should act like the normal `head` utility and print the expected number of lines from the given file.

````
$ ./head.py
Usage: head.py FILE [NUM_LINES]
$ ./head.py foo
foo is not a file
$ ./head.py files/issa.txt
Selected Haiku by Issa

Don’t worry, spiders,
$ ./head.py files/issa.txt 5
Selected Haiku by Issa

Don’t worry, spiders,
I keep house
casually.
````
