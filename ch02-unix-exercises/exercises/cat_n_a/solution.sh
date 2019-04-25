#!/usr/bin/env bash

set -u

if [[ $# -ne 1 ]]; then
    echo "Usage: cat-n.sh FILE"
    exit 1
fi

FILE=$1

if [[ ! -f "$FILE" ]]; then
    echo "$FILE is not a file"
    exit 1
fi

i=0
while read -r LINE; do
    i=$((i+1))
    echo "$i $LINE"
done < "$FILE"
