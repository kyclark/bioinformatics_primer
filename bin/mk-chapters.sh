#!/usr/bin/env bash

CHAPTERS=$(mktemp)
find . -mindepth 1 -maxdepth 1 -name ch\* -type d | sort > "$CHAPTERS"

while read -r CHAPTER; do
    echo "$CHAPTER"
    (cd "$CHAPTER" && make pdf)
done < "$CHAPTERS"
