#!/usr/bin/env bash

set -u

HELLO=${1:-"./hello.sh"}
NAMES="../../../inputs/1945-boys.txt"

if [[ ! -f "$NAMES" ]]; then
    echo "Missing NAMES \"$NAMES\""
    exit 1
fi

JOBS=$(mktemp)
i=0
while read -r NAME; do
    i=$((i+1))
    echo "$HELLO \"#$i $NAME\"" >> "$JOBS"
done < "$NAMES"

parallel < "$JOBS"

rm "$JOBS"
echo "Done."
