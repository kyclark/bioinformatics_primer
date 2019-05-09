#!/usr/bin/env bash

set -u

BOOK=$(mktemp)

cat /dev/null > "$BOOK"

i=0
#find . -maxdepth 2 -mindepth 2 -name \*.md -not -name README.md | sort > "$CHAPTERS"

CHAPTERS=$(mktemp)
find . -maxdepth 1 -mindepth 1 -name ch\* -type d | sort > "$CHAPTERS"
while read -r CHAPTER; do
    CH_NUM=$(echo "$CHAPTER" | perl -ne 's/\D//g; print(int($_))')

    MD=$(find "$CHAPTER" -maxdepth 1 -mindepth 1 -name \*.md -not -name README.md)

    printf "%3d: %s\n" $CH_NUM "$MD"

    echo "# Chapter $CH_NUM" >> "$BOOK"
    echo "" >> "$BOOK"
    cat "$MD" >> "$BOOK"

    #EX_DIR="$CHAPTER/exercises"
    #if [[ -d "$EX_DIR" ]]; then
    #    EXERCISES=$(mktemp)
    #    find "$EX_DIR" -mindepth 1 -maxdepth 1 -type d | sort > "$EXERCISES"

    #    EX_NUM=0
    #    while read -r EX_DIR; do
    #        README="$EX_DIR/README.md"
    #        EX_NUM=$((EX_NUM+1))

    #        if [[ -f "$README" ]]; then
    #            echo $README
    #            echo "# Exercise $EX_NUM: $(basename "$EX_DIR")" >> "$BOOK"
    #            cat "$README" >> "$BOOK"
    #        fi
    #    done < "$EXERCISES"
    #fi

    echo "" >> "$BOOK"
    echo '\pagebreak' >> "$BOOK"
    echo "" >> "$BOOK"
done < "$CHAPTERS"

pandoc "$BOOK" -o "PPDS.epub"
pandoc "$BOOK" -o "PPDS.pdf"

#rm "$BOOK"

echo "Done."
