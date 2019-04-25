#!/usr/bin/env bash

TMP=$(mktemp)
TMP=tmp

cat /dev/null > "$TMP"

i=0
for MD in $(find . -maxdepth 2 -mindepth 2 -name \*.md -not -name README.md | sort); do
    i=$((i+1))

    [[ $i -eq 11 ]] && continue
    printf "%3d: %s\n" $i "$MD"

    echo "# Chapter $i" >> "$TMP"
    echo "" >> "$TMP"
    cat "$MD" >> "$TMP"

    echo "" >> "$TMP"
    echo '\pagebreak' >> "$TMP"
    echo "" >> "$TMP"

    [[ $i -eq 12 ]] && break
done

for EXT in pdf epub; do
    #pandoc -F ../bin/include.hs "$TMP" -o "PPDS.$EXT"
    pandoc "$TMP" -o "PPDS.$EXT"
done

#rm "$TMP"

echo "Done."
