# cat_n.py

Create a Python program called `cat_n.py` that does the following:

* It should expect exactly one argument which is a regular file; if either condition fails, print a "Usage" statement
* It should print each line of the file argument preceeded by the line number which is right-justified in spaces and a colon. You may use format strings to make it look exactly like the output below, but the test is just checking for a leading space, some number(s), a colon, and whatever else.

Expected behavior:

````
$ ./cat_n.py
Usage: cat_n.py FILE
$ ./cat_n.py foo
foo is not a file
$ ./cat_n.py files/issa.txt
    1: Selected Haiku by Issa
    2:
    3: Don’t worry, spiders,
    4: I keep house
    5: casually.
    6:
    7: New Year’s Day—
    8: everything is in blossom!
    9: I feel about average.
   10:
   11: The snow is melting
   12: and the village is flooded
   13: with children.
   14:
   15: Goes out,
   16: comes back—
   17: the love life of a cat.
   18:
   19: Mosquito at my ear—
   20: does he think
   21: I’m deaf?
   22:
   23: Under the evening moon
   24: the snail
   25: is stripped to the waist.
   26:
   27: Even with insects—
   28: some can sing,
   29: some can’t.
   30:
   31: All the time I pray to Buddha
   32: I keep on
   33: killing mosquitoes.
   34:
   35: Napped half the day;
   36: no one
   37: punished me!
````
# Test Suite

A passing test suite looks like the following:

````
````
