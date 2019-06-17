# File Handling: Emulate "cat -n"

Create a Python program called `cat_n.py` that expects exactly one argument which is a regular file and prints usage statement if either condition fails. It should print each line of the file argument preceeded by the line number which is right-justified in spaces and a colon. You may the format '{:5}: {}' to make it look exactly like the output below, but the test is just checking for a leading space, some number(s), a colon, and the line of text.

````
$ ./cat_n.py
Usage: cat_n.py FILE
$ ./cat_n.py foo
foo is not a file
$ ./cat_n.py files/sonnet-29.txt
    1: Sonnet 29
    2: William Shakespeare
    3:
    4: When, in disgrace with fortune and men’s eyes,
    5: I all alone beweep my outcast state,
    6: And trouble deaf heaven with my bootless cries,
    7: And look upon myself and curse my fate,
    8: Wishing me like to one more rich in hope,
    9: Featured like him, like him with friends possessed,
   10: Desiring this man’s art and that man’s scope,
   11: With what I most enjoy contented least;
   12: Yet in these thoughts myself almost despising,
   13: Haply I think on thee, and then my state,
   14: (Like to the lark at break of day arising
   15: From sullen earth) sings hymns at heaven’s gate;
   16: For thy sweet love remembered such wealth brings
   17: That then I scorn to change my state with kings.
````
