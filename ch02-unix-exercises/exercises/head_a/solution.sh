#!/usr/bin/env bash

set -u

if [[ $# -lt 1 ]]; then
    echo "Usage: head.sh FILE NUM"
    exit 1
fi

FILE=$1
NUM=${2:-3}

if [[ ! -f "$FILE" ]]; then
    echo "$FILE is not a file"
    exit 1
fi

i=0
while read -r LINE; do
    i=$((i+1))
    echo $LINE
    if [[ $i -eq $NUM ]]; then
        break
    fi
done < "$FILE"
