#!/usr/bin/env bash

set -u

PREFIX=${1:-"[A-Z]"}
DATA_DIR="gapminder"
FILES=$(mktemp)

for FILE in $(find "$DATA_DIR" -type f -iname $PREFIX\*.cc.txt | sed "s/\.cc\.txt//" | sort)
do
    echo $(basename "$FILE") >> "$FILES"
done

NUM=$(wc -l "$FILES" | awk '{print $1}')

if [[ $NUM -eq 0 ]]; then
    echo "There are no countries starting with \"$PREFIX\""
    exit 1
else
    cat -n "$FILES"
fi
