#!/usr/bin/env python3
"""
Author : kyclark
Date   : 2019-04-09
Purpose: Tea Timer
"""

import os
import sys
import time


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    wait_time = int(args[0]) if args else 120

    if wait_time < 60:
        wait_time *= 60

    print('Your tea will be ready in {} seconds...'.format(wait_time))
    time.sleep(wait_time)

    print('Tea is ready')


# --------------------------------------------------
main()
