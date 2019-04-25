# hello.sh

Create a bash script called "hello.sh" with the following behavior:

* If there are no arguments, it should print a "Usage" and exit *with an error code*
* Your program will expect to receive a "greeting" in `$1` and possibly a name in `$2`; if there is no second argument, use "Human" as the default
* If there are more than two arguments, print a "Usage" and exit *with an error code*
* Print the greeting, a comma and space, the name, and an exclamation point

Here is how it should look:

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

You have been provided a `Makefile` that will run a test suite. This is what it should look like when all tests are passing:

````
$ make test
python3 -m pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.7.0, pytest-3.8.0, py-1.6.0, pluggy-0.7.1 -- /anaconda3/bin/python3
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/biosys-analytics/assignments/02-bash-scripting-grad, inifile:
plugins: remotedata-0.3.0, openfiles-0.3.0, doctestplus-0.1.3, arraydiff-0.2
collected 5 items

test.py::test_exists PASSED                                              [ 20%]
test.py::test_usage PASSED                                               [ 40%]
test.py::test_hello_too_many PASSED                                      [ 60%]
test.py::test_hello PASSED                                               [ 80%]
test.py::test_gap PASSED                                                 [100%]

=========================== 5 passed in 0.46 seconds ===========================
````
