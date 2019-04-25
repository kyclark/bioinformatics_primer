#!/bin/bash

set -u

if [[ $# -ne 1 ]]; then
    printf "Usage: %s DIR\n" "$(basename "$0")"
    exit 1
fi

DIR=$1
TMP=$(mktemp)
find "$DIR" -type f -name \*.fa > "$TMP"
NUM_FILES=$(wc -l "$TMP" | awk '{print $1}')

if [[ $NUM_FILES -lt 1 ]]; then
    echo "Found no .fa files in $DIR"
    exit 1
fi

NUM_SEQS=0
while read -r FILE; do
    NUM_SEQ=$(grep -c '^>' "$FILE")
    NUM_SEQS=$((NUM_SEQS + NUM_SEQ))
    printf "%10d %s\n" "$NUM_SEQ" "$(basename "$FILE")"
done < "$TMP"

rm "$TMP"

echo "Done, found $NUM_SEQS sequences in $NUM_FILES files."
