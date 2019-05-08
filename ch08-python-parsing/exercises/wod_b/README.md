# Workout Of (the) Day (WOD)

Write a Python program called `wod.py` that will create a Workout Of (the) Day (WOD) from a list of exercises provided in CSV format (default `wod.csv`). Accept a `-n|--num_exercises` argument (default 4) to determine the sample size from your exercise list. Also accept a `-e|--easy` flag to indicate that the reps should be cut in half. Finally accept a `-s|--seed` argument for `random.seed` for testing purposes.

# Expected Behavior

````
$ ./wod.py -h
usage: wod.py [-h] [-f str] [-s int] [-n int] [-e]

Create Workout Of (the) Day (WOD)

optional arguments:
  -h, --help            show this help message and exit
  -f str, --file str    CSV input file of exercises (default: wod.csv)
  -s int, --seed int    Random seed (default: None)
  -n int, --num_exercises int
                        Number of exercises (default: 4)
  -e, --easy            Make it easy (default: False)
$ ./wod.py
Exercise       Reps
-------------  ------
HSPU           5-20
Jumping Jacks  25-75
Squats         20-50
Pushups        25-75
$ ./wod.py -s 1
Exercise       Reps
-------------  ------
Pushups        25-75
Jumping Jacks  25-75
Situps         40-100
Pullups        10-30
$ ./wod.py -s 1 -e
Exercise       Reps
-------------  ------
Pushups        12-37
Jumping Jacks  12-37
Situps         20-50
Pullups        5-15
$ ./wod.py -f wod2.csv -n 5
Exercise                Reps
----------------------  ------
Masochistic Elbowdowns  25-75
Squatting Chinups       20-50
Existential Earflaps    20-40
Flapping Leg Raises     10-30
Rock Squats             20-50
````

# Test Suite

A passing test suite looks like the following:

````
$ make test
pytest -v test.py
============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-4.2.0, py-1.7.0, pluggy-0.8.1 -- /anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/python/practical_python_for_data_science/ch08-python-parsing/exercises/wod_b, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.2.0, arraydiff-0.3
collected 5 items

test.py::test_usage PASSED                                               [ 20%]
test.py::test_runs01 PASSED                                              [ 40%]
test.py::test_runs02 PASSED                                              [ 60%]
test.py::test_runs03 PASSED                                              [ 80%]
test.py::test_runs04 PASSED                                              [100%]

=========================== 5 passed in 0.50 seconds ===========================
````
