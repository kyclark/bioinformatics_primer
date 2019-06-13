#!/bin/bash

set -u

GREETING=""
NAME="Stranger"
EXCITED=0

function USAGE() {
    printf "Usage:\n  %s -g GREETING [-e] [-n NAME]\n\n" $(basename $0)
    echo "Required arguments:"
    echo " -g GREETING"
    echo
    echo "Options:"
    echo " -n NAME ($NAME)"
    echo " -e Print exclamation mark (default yes)"
    echo 
    exit ${1:-0}
}

[[ $# -eq 0 ]] && USAGE 1

while getopts :g:n:eh OPT; do
  case $OPT in
    h)
      USAGE
      ;;
    e)
      EXCITED=1
      ;;
    g)
      GREETING="$OPTARG"
      ;;
    n)
      NAME="$OPTARG"
      ;;
    :)
      echo "Error: Option -$OPTARG requires an argument."
      exit 1
      ;;
    \?)
      echo "Error: Invalid option: -${OPTARG:-""}"
      exit 1
  esac
done

[[ -z "$GREETING" ]] && USAGE 1
PUNCTUATION="."
[[ $EXCITED -ne 0 ]] && PUNCTUATION="!"

echo "$GREETING, $NAME$PUNCTUATION"
