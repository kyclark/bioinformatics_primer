#!/usr/bin/env python3

import logging
import os
import sys

prg = sys.argv[0]
prg_name, _ = os.path.splitext(os.path.basename(prg))

logging.basicConfig(
    filename=prg_name + '.log',
    filemode='w',
    level=logging.DEBUG
)

logging.debug('DEBUG!')
logging.critical('CRITICAL!')
