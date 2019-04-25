#!/bin/bash

FILE=${1:-'srr.txt'}
while read -r LINE; do
    echo "LINE \"$LINE\""
done < "$FILE"
