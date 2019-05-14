# hello.sh

Create a bash script called `hello.sh` that accepts one or two arguments. If there are no arguments, it should print a "Usage" and exit *with an error code*. Your program will expect to receive a "greeting" in `$1` and possibly a name in `$2`; if there is no second argument, use "Human" as the default. If there are more than two arguments, print a "Usage" and exit *with an error code*. Print the greeting, a comma and space, the name, and an exclamation point.

# Expected Behavior

````
$ ./hello.sh
Usage: hello.sh GREETING [NAME]
$ ./hello.sh That\'ll do pig
Usage: hello.sh GREETING [NAME]
$ ./hello.sh "That'll do" pig
That'll do, pig!
$ ./hello.sh "Top o' the morning"
Top o' the morning, Human!
$ ./hello.sh "Greetings" "Earthling"
Greetings, Earthling!
````

# Testing

A passing test suite looks like this:

````
$ make test
pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.7.3, pytest-4.3.1, py-1.8.0, pluggy-0.9.0 -- /Users/kyclark/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/python/practical_python_for_data_science/ch02-unix-exercises/exercises/hello_b, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.3.0, arraydiff-0.3
collected 3 items

test.py::test_usage PASSED                                               [ 33%]
test.py::test_hello_too_many PASSED                                      [ 66%]
test.py::test_hello PASSED                                               [100%]

=========================== 3 passed in 0.09 seconds ===========================
````
