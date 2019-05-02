# Article Selector

Make a Python program called `article.py` that prepends before the given "word" (it may not really be a word) the article "a" if the word begins with a consonant or "an" if it begins with a vowel. If given no arguments, the program should provide a usage statement.

# Expected Behavior

````
$ ./article.py
Usage: article.py WORD
$ ./article.py foo
a foo
$ ./article.py oof
an oof
````

# Test Suite

Either run `make test` (if you have `make`) or `pytest -v test.py`. A passing test suite looks like this:

````
$ make test
pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-4.2.0, py-1.7.0, pluggy-0.8.1 -- /anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/python/practical_python_for_data_science/ch04-python-intro/exercises/article_a, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.2.0, arraydiff-0.3
collected 2 items

test.py::test_usage PASSED                                               [ 50%]
test.py::test_works PASSED                                               [100%]

=========================== 2 passed in 0.47 seconds ===========================
````
