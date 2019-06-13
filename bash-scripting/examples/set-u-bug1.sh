#!/bin/bash

set -u

if [[ $# -gt 0 ]]; then
  echo $THIS_IS_A_BUG; # never initialized
fi

echo "OK";
