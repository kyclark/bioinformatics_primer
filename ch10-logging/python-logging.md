# Logging in Python

So far we've use `print` statements that go to STDOUT and the `warn` function that makes is slightly more convenient to write to STDERR. The trouble with this approach to writing and debugging code is that you need to remove all the `print`/`warn` statements prior to releasing your code or running your tests. With the `logging` module (https://docs.python.org/3/library/logging.html), you can sprinkle messages to yourself liberally throughout your code and chose *at run time* which ones to see. 

Like with `random.seed`, calls to the `logging` module affect the **global state** of how logging happens. First you need to set up how the logging will happen using the `basicConfig` (https://docs.python.org/3/library/logging.html#logging.basicConfig). Typically you will set log message to go to a `filename` (if you don't indicate a filename then messages go to STDERR) with the `filemode` of "w" (write, which will overwrite existing files; default is "a" for append) at some `level` like `logging.DEBUG` (default is `logging.NOTSET` so everything prints). Here is a script (in `examples`) that does that:

````
$ cat -n basic.py
     1	#!/usr/bin/env python3
     2
     3	import logging
     4	import os
     5	import sys
     6
     7	prg = sys.argv[0]
     8	prg_name, _ = os.path.splitext(os.path.basename(prg))
     9	logging.basicConfig(
    10	    filename=prg_name + '.log',
    11	    filemode='w',
    12	    level=logging.DEBUG
    13	)
    14
    15	logging.debug('DEBUG!')
    16	logging.critical('CRITICAL!')
````

Before running the program, see that there is no log file:

````
$ ls
basic.py* long.py*
````

Run it, and see that `basic.log` has been created:

````
$ ls
basic.log  basic.py*  long.py*
$ cat basic.log
DEBUG:root:DEBUG!
CRITICAL:root:CRITICAL!
````

The key is to understand the hierarchy of the levels:

1. CRITICAL
2. ERROR
3. WARNING
4. INFO
5. DEBUG
6. NOTSET

The log level includes everything above the level you set. As in the above program, we set it to `logging.DEBUG` and so a call to `critical` was included. If you change the program to `logging.CRITICAL`, then `error` through `debug` calls are not emitted:

````
$ cat -n basic.py
     1	#!/usr/bin/env python3
     2
     3	import logging
     4	import os
     5	import sys
     6
     7	prg = sys.argv[0]
     8	prg_name, _ = os.path.splitext(os.path.basename(prg))
     9	logging.basicConfig(
    10	    filename=prg_name + '.log',
    11	    filemode='w',
    12	    level=logging.CRITICAL
    13	)
    14
    15	logging.debug('DEBUG!')
    16	logging.critical('CRITICAL!')
$ ./basic.py
$ cat basic.log
CRITICAL:root:CRITICAL!
````

If you find yourself repeatedly debugging some program or just need to know information about how it is proceeding, then `logging` is for you. Maybe you have some functions or system calls that take a long time; sometimes you want to monitor how they are going and other times (e.g., running unattended on the HPC) you don't. Here is a program that logs random levels and then sleeps for one second. To see how this could be useful, open two terminals and navigate to the `examples` directory. 

Here is the program:

````
$ cat -n long.py
     1	#!/usr/bin/env python3
     2
     3	import argparse
     4	import logging
     5	import os
     6	import random
     7	import sys
     8	import time
     9
    10
    11	# --------------------------------------------------
    12	def get_args():
    13	    """get command-line arguments"""
    14	    parser = argparse.ArgumentParser(
    15	        description='Demonstrate logging',
    16	        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    17
    18	    parser.add_argument(
    19	        '-d', '--debug', help='Debug mode', action='store_true')
    20
    21	    return parser.parse_args()
    22
    23
    24	# --------------------------------------------------
    25	def main():
    26	    """Make a jazz noise here"""
    27	    args = get_args()
    28
    29	    prg = sys.argv[0]
    30	    prg_name, _ = os.path.splitext(os.path.basename(prg))
    31	    logging.basicConfig(
    32	        filename=prg_name + '.log',
    33	        filemode='a',
    34	        level=logging.DEBUG if args.debug else logging.CRITICAL)
    35
    36	    logging.debug('Starting')
    37	    for i in range(1, 11):
    38	        method = random.choice([
    39	            logging.info, logging.warning, logging.error, logging.critical,
    40	            logging.debug
    41	        ])
    42	        method('{}: Hey!'.format(i))
    43	        time.sleep(1)
    44
    45	    logging.debug('Done')
    46
    47	    print('Done.')
    48
    49
    50	# --------------------------------------------------
    51	if __name__ == '__main__':
    52	    main()
````

Start running `long.py` in one terminal, then execute `tail -f long.log` in the other where `tail` is the program to show you the end of a file and `-f` tells `tail` to stay running and "follow" the file as it grows. (Use CTRL-C to stop following.)  Following is what I see when I run `long.py`. Note that, since I didn't set the `-d|--debug` flag, my program will only log *critical* errors:

````
CRITICAL:root:5: Hey!
CRITICAL:root:8: Hey!
````

And when I run `long.py -d`, everything from "debug" on up is displayed:

````
DEBUG:root:Starting
WARNING:root:1: Hey!
ERROR:root:2: Hey!
DEBUG:root:3: Hey!
DEBUG:root:4: Hey!
CRITICAL:root:5: Hey!
INFO:root:6: Hey!
ERROR:root:7: Hey!
INFO:root:8: Hey!
DEBUG:root:9: Hey!
CRITICAL:root:10: Hey!
DEBUG:root:Done
````