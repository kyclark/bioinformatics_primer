#!/usr/bin/env bash

set -u

MAX=25
WORDS=/usr/share/dict/words
CORES=4

if [[ ! -f "$WORDS" ]]; then
    echo "WORDS \"$WORDS\" is not a file"
    exit 1
fi

TMP=$(mktemp)
i=0
while read -r WORD; do
    i=$((i+1))
    echo "echo \"$i $WORD\"" >> "$TMP"
    if [[ $i -eq $MAX ]]; then
        break
    fi
done < "$WORDS"

echo "Starting parallel on $CORES cores"
parallel -j $CORES --halt soon,fail=1 < "$TMP"
echo "Finished parallel"
