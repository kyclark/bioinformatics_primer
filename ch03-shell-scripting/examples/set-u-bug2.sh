#!/bin/bash

set -u

GREETING="Hi"
if [[ $# -gt 0 ]]; then
  GRETING=$1 # misspelled
fi

echo $GREETING
