# Greeter: Positional Command-line Arguments

Write a Python program named `hello.py` that warmly greets the names you provide.  When there are two names, join them with "and."  When there are three or more, join them on commas (INCLUDING THE OXFORD WE ARE NOT SAVAGES) and "and." If no names are supplied, print a usage.

````
$ ./hello.py
Usage: hello.py NAME [NAME...]
$ ./hello.py Alice
Hello to the 1 of you: Alice!
$ ./hello.py Mike Carol
Hello to the 2 of you: Mike and Carol!
$ ./hello.py Greg Peter Bobby Marcia Jane Cindy
Hello to the 6 of you: Greg, Peter, Bobby, Marcia, Jane, and Cindy!
````
