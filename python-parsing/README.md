# Parsing with Python

> Programming is the art of doing one thing at a time. -- Michael Feathers

We'll use the term "parsing" to mean deriving meaning from structured text. In this chapter, we'll look at parsing command-line arguments and common file file formats in bioinformatics like CSV, FASTA/Q, and GFF.

## Command-line Arguments

If you've been using `new_py.py -a` to create new programs, you've already been using a parser -- one that uses the `argparse` module to derive meaning from command-line arguments that may or may not have flags or be defined by positions. Let's create a new program and see how it works:

````
$ new_py.py -a test
Done, see new script "test.py."
````

If you check out the new script, it has a `get_args` function that will show you how to create named arguments for strings, integers, booleans, and positional arguments:

````
     1	#!/usr/bin/env python3
     2	"""
     3	Author : kyclark
     4	Date   : 2019-02-19
     5	Purpose: Rock the Casbah
     6	"""
     7
     8	import argparse
     9	import sys
    10
    11
    12	# --------------------------------------------------
    13	def get_args():
    14	    """get command-line arguments"""
    15	    parser = argparse.ArgumentParser(
    16	        description='Argparse Python script',
    17	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    18
    19	    parser.add_argument(
    20	        'positional', metavar='str', help='A positional argument')
    21
    22	    parser.add_argument(
    23	        '-a',
    24	        '--arg',
    25	        help='A named string argument',
    26	        metavar='str',
    27	        type=str,
    28	        default='')
    29
    30	    parser.add_argument(
    31	        '-i',
    32	        '--int',
    33	        help='A named integer argument',
    34	        metavar='int',
    35	        type=int,
    36	        default=0)
    37
    38	    parser.add_argument(
    39	        '-f', '--flag', help='A boolean flag', action='store_true')
    40
    41	    return parser.parse_args()
    42
    43
    44	# --------------------------------------------------
    45	def warn(msg):
    46	    """Print a message to STDERR"""
    47	    print(msg, file=sys.stderr)
    48
    49
    50	# --------------------------------------------------
    51	def die(msg='Something bad happened'):
    52	    """warn() and exit with error"""
    53	    warn(msg)
    54	    sys.exit(1)
    55
    56
    57	# --------------------------------------------------
    58	def main():
    59	    """Make a jazz noise here"""
    60	    args = get_args()
    61	    str_arg = args.arg
    62	    int_arg = args.int
    63	    flag_arg = args.flag
    64	    pos_arg = args.positional
    65
    66	    print('str_arg = "{}"'.format(str_arg))
    67	    print('int_arg = "{}"'.format(int_arg))
    68	    print('flag_arg = "{}"'.format(flag_arg))
    69	    print('positional = "{}"'.format(pos_arg))
    70
    71
    72	# --------------------------------------------------
    73	if __name__ == '__main__':
    74	    main()
````

If you run without any arguments or with `-h|--help`, you get a usage statement:

````
$ ./test.py
usage: test.py [-h] [-a str] [-i int] [-f] str
test.py: error: the following arguments are required: str
[cholla@~/work/biosys-analytics/lectures/09-python-parsing]$ ./test.py -h
usage: test.py [-h] [-a str] [-i int] [-f] str

Argparse Python script

positional arguments:
  str                A positional argument

optional arguments:
  -h, --help         show this help message and exit
  -a str, --arg str  A named string argument (default: )
  -i int, --int int  A named integer argument (default: 0)
  -f, --flag         A boolean flag (default: False)
````

And the `argparse` module is able to turn the command line arguments into useful information:

````
$ ./test.py -a foo -i 42 -f ABCDE
str_arg = "foo"
int_arg = "42"
flag_arg = "True"
positional = "ABCDE"
````

If you try to write the code to parse `-a foo -i 42 -f ABCDE`, you will quickly appreciate how much effort using this module will save you!




## JSON

JSON stands for JavaScript Object Notation, and it has become the lingua franca of data exchange on the Internet. For our example, I will use the JSON that is returned by https://www.imicrobe.us/api/v1/samples/578. We need to `import json` and use `json.load` to read from an open file handle (there is also `loads` -- load string) to parse the data from JSON into a Python dictionary. We could `print` that, but it's not nearly as pretty as printing the JSON which we can do with `json.dumps` (dump string) and the keyword argument `indent=4` to get nice indentation.

````
$ cat -n json_parse.py
     1	#!/usr/bin/env python3
     2
     3	import json
     4
     5	file = '578.json'
     6	data = json.load(open(file))
     7	print(json.dumps(data, indent=4))
$ ./json_parse.py | head -12
{
    "sample_id": 578,
    "project_id": 26,
    "sample_acc": "CAM_SMPL_GS108",
    "sample_name": "GS108",
    "sample_type": "Metagenome",
    "sample_description": "GS108",
    "url": "",
    "creation_date": "2018-07-06T04:43:09.000Z",
    "project": {
        "project_id": 26,
        "project_code": "CAM_PROJ_GOS",
````

If you `head 578.json`, you will see there is no whitespace, so this is a nicer way to look at the data; however, if all we wanted was to look at pretty JSON, we could do this:

````
$ python -m json.tool 578.json
````
