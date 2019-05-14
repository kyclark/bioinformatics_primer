# Vowel Counter

Write a Python program called `vowel_counter.py` that counts the number of vowels in a single string. Be sure your subject and verb agree in number, and use proper plurals.

# Expected Behavior

````
$ ./vowel_counter.py
Usage: vowel_counter.py STRING
$ ./vowel_counter.py for
There is 1 vowel in "for."
$ ./vowel_counter.py elliptical
There are 4 vowels in "elliptical."
$ ./vowel_counter.py YYZ
There are 0 vowels in "YYZ."
````

# Discussion

This program has no options or flags, just a single position argument, so you can use `new_py.py` in the (default) simple mode.

There are many ways you can count the vowels in the input string. One way is you could use a `for` loop that iterates over a list of vowels and counts how many times that vowels occurs in the word you were given.  (Hint: there is a method in the `str` class that will do exactly this!)  Here is some pseudo-code:

```
create a variable to hold the count
for vowels in vowels:
    how often does vowel occur in word?
    add that number to the count
```

# Tests

A successful test suite looks like this:

````
$ make test
pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.7.3, pytest-4.3.1, py-1.8.0, pluggy-0.9.0 -- /Users/kyclark/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/python/practical_python_for_data_science/ch04-python-intro/exercises/vowel_counter_a, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.3.0, arraydiff-0.3
collected 7 items

test.py::test_usage_counter PASSED                                       [ 14%]
test.py::test_01 PASSED                                                  [ 28%]
test.py::test_02 PASSED                                                  [ 42%]
test.py::test_03 PASSED                                                  [ 57%]
test.py::test_04 PASSED                                                  [ 71%]
test.py::test_05 PASSED                                                  [ 85%]
test.py::test_06 PASSED                                                  [100%]

=========================== 7 passed in 0.26 seconds ===========================
````
