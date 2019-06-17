# Parsing Date Formats with Regular Expressions 

Write a Python program called `dates.py` that takes as a single, positional argument a string and attempt to parse it as one of the given date formats. If given no argument, it should print a usage statement. It does not need to respond to `-h|--help`, so you could use `new_py.py` without the argparse flag.

````
$ ./dates.py
Usage: dates.py DATE
````

If you are able to match one of the acceptable format strings below, print the date in a standard "YYYY-MM-DD" format. If only given year and month, e.g. "12/06," use "1" as the day. When there is a range of dates (e.g., "2015-01/2015-02"), only parse the first one.

These are the formats you will be given:

````
$ cat eg_dates.txt
2012-03-09T08:59
2012-03-09T08:59:03
2017-06-16Z
2015-01
2015-01/2015-02
2015-01-03/2015-02-14
20100910
12/06
2/14
2/14-12/15
2017-06-16Z
Dec-2015
Dec, 2015
March-2017
April, 2017
````

Here is the expected output:

````
$ while read -r DATE; do ./dates.py "$DATE"; done < eg_dates.txt
2012-03-09
2012-03-09
2017-06-16
2015-01-01
2015-01-01
2015-01-03
2010-09-10
2006-12-01
2014-02-01
2014-02-01
2017-06-16
2015-12-01
2015-12-01
2017-03-01
2017-04-01
````

If you are unable to parse the argument, print "No match":

````
$ ./dates.py foo
No match
$ ./dates.py 1999.12.31
No match
````

While there are date parsing modules, I do not want you to use those in your code. Please write your own regular expressions and parsing code.
