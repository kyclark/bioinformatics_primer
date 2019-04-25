#!/bin/bash

set -u

DIR=${1:-$PWD}

if [[ ! -d "$DIR" ]]; then
    echo "$DIR is not a directory"
    exit 1
fi

i=0
for FILE in $DIR/*; do
    let i++
    printf "%3d: %s\n" $i $(basename "$FILE")
done
