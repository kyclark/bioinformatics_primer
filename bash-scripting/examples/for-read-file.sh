#!/bin/bash

FILE=${1:-'srr.txt'}
for LINE in $(cat "$FILE"); do
    echo "LINE \"$LINE\""
done
