#!/bin/bash

FILE='meta.tab'
while read -r SITE LOC; do
    echo "$SITE is located at \"$LOC\""
done < "$FILE"
