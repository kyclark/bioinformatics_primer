#!/usr/bin/env bash

TMP=$(mktemp)

cat /dev/null > "$TMP"

i=0
for MD in $(find . -maxdepth 2 -mindepth 2 -name \*.md -not -name README.md | sort); do
    i=$((i+1))

    printf "%3d: %s\n" $i "$MD"

    echo "# Chapter $i" >> "$TMP"
    echo "" >> "$TMP"
    cat "$MD" >> "$TMP"

    echo "" >> "$TMP"
    echo '\pagebreak' >> "$TMP"
    echo "" >> "$TMP"
done

pandoc "$TMP" -o "PPDS.epub"
iconv -t utf-8 "$TMP" | pandoc -o PPDS.pdf --latex-engine=xelatex
#pandoc "$TMP" -o PPDS.pdf --latex-engine=xelatex
#pandoc "$TMP" -o PPDS.pdf --latex-engine=xelatex

rm "$TMP"

echo "Done."
