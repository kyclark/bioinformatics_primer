#!/usr/bin/env bash

TMP=$(mktemp)

cat /dev/null > "$TMP"

i=0
for MD in $(find . -maxdepth 2 -mindepth 2 -name \*.md | sort); do
    i=$((i+1))
    printf "%3d: %s\n" $i "$MD"

    echo "# Chapter $i" >> "$TMP"
    echo "" >> "$TMP"
    cat "$MD" >> "$TMP"

    echo "" >> "$TMP"
    echo '\pagebreak' >> "$TMP"
    echo "" >> "$TMP"
done

for EXT in pdf epub; do
    pandoc -F ../bin/include.hs "$TMP" -o "biosys.$EXT"
done

rm "$TMP"

echo "Done."
