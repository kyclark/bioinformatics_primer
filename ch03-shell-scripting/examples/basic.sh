#!/bin/bash

set -u

IN_DIR=""
OUT_DIR="$PWD/$(basename "$0" '.sh')-out"

function lc() {
    wc -l "$1" | awk '{print $1}'
}

function USAGE() {
    printf "Usage:\n  %s -i IN_DIR -o OUT_DIR\n\n" "$(basename "$0")"

    echo "Required arguments:"
    echo " -i IN_DIR"
    echo "Options:"
    echo " -o OUT_DIR"
    echo 
    exit "${1:-0}"
}

[[ $# -eq 0 ]] && USAGE 1

while getopts :i:o:h OPT; do
    case $OPT in
        h)
            USAGE
            ;;
        i)
            IN_DIR="$OPTARG"
            ;;
        o)
            OUT_DIR="$OPTARG"
            ;;
        :)
            echo "Error: Option -$OPTARG requires an argument."
            exit 1
            ;;
        \?)
            echo "Error: Invalid option: -${OPTARG:-""}"
            exit 1
    esac
done

if [[ -z "$IN_DIR" ]]; then
    echo "IN_DIR is required"
    exit 1
fi

if [[ ! -d "$IN_DIR" ]]; then
    echo "IN_DIR \"$IN_DIR\" is not a directory."
    exit 1
fi

echo "Started $(date)"

FILES_LIST=$(mktemp)
find "$IN_DIR" -type f -name \*.sh > "$FILES_LIST"
NUM_FILES=$(lc "$FILES_LIST")

if [[ $NUM_FILES -gt 0 ]]; then
    echo "Will process NUM_FILES \"$NUM_FILES\""

    [[ ! -d $OUT_DIR ]] && mkdir -p "$OUT_DIR"

    i=0
    while read -r FILE; do
        BASENAME=$(basename "$FILE")
        let i++
        printf "%3d: %s\n" $i "$BASENAME"
        wc -l "$FILE" > "$OUT_DIR/$BASENAME"
    done < "$FILES_LIST"

    rm "$FILES_LIST"
    echo "See results in OUT_DIR \"$OUT_DIR\""
else
    echo "No files found in \"$IN_DIR\""
fi

echo "Finished $(date)"
