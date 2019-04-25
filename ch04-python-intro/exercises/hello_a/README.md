# Hello, Python!

Write a Python program named "hello.py" that warmly greets the names you provide.  When there are two names, join them with "and."  When there are three or more, join them on commas (INCLUDING THE OXFORD WE ARE NOT SAVAGES) and "and." If no names are supplied, print a usage:

```
$ ./hello.py
Usage: hello.py NAME [NAME2 ...]
$ ./hello.py Alice
Hello to the 1 of you: Alice!
$ ./hello.py Mike Carol
Hello to the 2 of you: Mike and Carol!
$ ./hello.py Greg Peter Bobby Marcia Jane Cindy
Hello to the 6 of you: Greg, Peter, Bobby, Marcia, Jane, and Cindy!
```

Your program needs to:

* Check the number of arguments
* If there are no arguments, print a "Usage" and exit with an error
* print "Hello to the N of you: ...!" where "N" is the number of arguments and "..." is the properly formatted as shown above for 1, 2, or >2 arguments

Think about how you solved these problems in bash:

* How do you find the number of arguments to your program?
* How do you print a usage statement?
* How do you exit with an error?
* How do you check for a condition, e.g., I have just one argument?
* How do you check for a second condition, e.g., I have two arguments?
* How do you check for a third/final condition, e.g., I have more than two arguments?
* How do you inspect the methods that Python lists have?

# Tests

A successful test suite looks like this:

```
$ make test
pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-4.2.0, py-1.7.0, pluggy-0.8.1 -- /anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/python/practical_python_for_data_science/ch04-python-intro/exercises/hello_a, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.2.0, arraydiff-0.3
collected 2 items

test.py::test_usage PASSED                                               [ 50%]
test.py::test_runs PASSED                                                [100%]

=========================== 2 passed in 0.19 seconds ===========================
```
