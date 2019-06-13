#!/usr/bin/env bash

JOBS=$(mktemp)

for i in $(seq 1 30); do
    echo "echo $i" >> "$JOBS"
done

NUM_JOBS=$(wc -l "$JOBS" | awk '{print $1}')

if [[ $NUM_JOBS -gt 0 ]]; then
    echo "Running $NUM_JOBS jobs"
    parallel -j 8 --halt soon,fail=1 < "$JOBS"
fi

[[ -f "$JOBS" ]] && rm "$JOBS"

echo "Done."
