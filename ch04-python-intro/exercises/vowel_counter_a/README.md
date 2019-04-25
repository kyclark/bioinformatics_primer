# Vowel Counter

Write a Python program called `vowel_counter.py` that counts the number of vowels in a single string. Be sure your subject and verb agree in number, and use proper plurals.

```
$ ./vowel_counter.py
Usage: vowel_counter.py STRING
$ ./vowel_counter.py for
There is 1 vowel in "for."
$ ./vowel_counter.py elliptical
There are 4 vowels in "elliptical."
$ ./vowel_counter.py YYZ
There are 0 vowels in "YYZ."
```

You can solve this exercise in many ways.  For example, you could use a `for` loop that iterates over a list of vowels and counts how many times that vowels occurs in the word you were given.  (Hint: there is a method in the `str` class that will do exactly this!)  Here is some pseudo-code:

```
create a variable to hold the count
for vowels in vowels:
    how often does vowel occur in word?
    add that number to the count
```

# Tests

A successful test suite looks like this:

```
$ make test
python3 -m pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.5.4, pytest-3.2.1, py-1.4.34, pluggy-0.4.0 -- /Users/kyclark/anaconda3/bin/python3
cachedir: .cache
rootdir: /Users/kyclark/work/secret-book/problems/hello-py, inifile:
collected 4 items

test.py::test_exists PASSED
test.py::test_usage PASSED
test.py::test_hello PASSED
test.py::test_counter PASSED

=========================== 4 passed in 0.33 seconds ===========================
```

# Grading

All tests must pass to receive credit.

# Help

Please feel free to email me (kyclark), stop by my office (Shantz 626), or
chat with me on Slack (abe487.slack.com).
