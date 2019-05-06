# Column

Create a Python program called `column.py` that takes a list of words and creates a columnar output of each word and their length. If given no words as positional, command-line arguments, print a usage statement. For the output, first print a header of "word" and "len", then lines which are the width of the longest word and the longest numbers with a minimum for each of the column headers themselves. The words should be left-justified in the first column and the numbers should be right-justified in the second column.

# Expected Behavior

````
$ ./column.py
Usage: column.py WORD [WORD...]
$ ./column.py a an the
word  len
----  ---
a       1
an      2
the     3
$ ./column.py `cat out/1.in`
word               len
-----------------  ---
Iphis                5
cyclone              7
dare                 4
umbraculiferous     15
indescribableness   17
prattling            9
pediculine          10
pondwort             8
lava                 4
adipoma              7
````

# Test Suite

A passing test suite should look like this:

$ make test
python3 -m pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-4.2.0, py-1.7.0, pluggy-0.8.1 -- /anaconda3/bin/python3
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/python/practical_python_for_data_science/ch05-python-strings-lists-tuples/exercises/columns_b, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.2.0, arraydiff-0.3
collected 2 items

test.py::test_usage PASSED                                               [ 50%]
test.py::test_runs PASSED                                                [100%]

=========================== 2 passed in 0.28 seconds ===========================````
