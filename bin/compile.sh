#!/usr/bin/env bash

set -u

BOOK=$(mktemp)

echo "# Intro" > "$BOOK"
cat README.md >> "$BOOK"
echo "" >> "$BOOK"
echo '\pagebreak' >> "$BOOK"
echo "" >> "$BOOK"

CHAPTERS=$(mktemp)
find . -maxdepth 1 -mindepth 1 -name ch\* -type d | sort > "$CHAPTERS"
while read -r CHAPTER; do
    CH_NUM=$(echo "$CHAPTER" | perl -ne 's/\D//g; print(int($_))')

    MD=$(find "$CHAPTER" -maxdepth 1 -mindepth 1 -name \*.md -not -name README.md)

    printf "%3d: %s\n" $CH_NUM "$MD"

    echo "# Chapter $CH_NUM" >> "$BOOK"
    echo "" >> "$BOOK"
    cat "$MD" >> "$BOOK"
    echo "" >> "$BOOK"
    echo '\pagebreak' >> "$BOOK"
    echo "" >> "$BOOK"
done < "$CHAPTERS"

pandoc "$BOOK" -o "PPDS.epub"
pandoc "$BOOK" -o "PPDS.pdf"

rm "$BOOK"

echo "Done."
