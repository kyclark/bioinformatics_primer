#!/bin/sh

set -u

if [[ $# -eq 0 ]]; then
    printf "Usage: %s FILE\n" "$(basename "$0")"
    exit 1
fi

FILE=$1

if [[ ! -f "$FILE" ]]; then
    echo "FILE \"$FILE\" is not a file"
    exit 1
fi

BASENAME=$(basename "$FILE")
FILE_DIR=$(cd "$(dirname "$FILE")" && pwd)
DEST_DIR=$(echo "$FILE_DIR" | perl -pe "s{$WORK}{kyclark/applications}")

echo "Deleting file \"$DEST_DIR/$BASENAME\""
files-delete "$DEST_DIR/$BASENAME"

files-upload -F "$BASENAME" "$DEST_DIR"

echo "Done."
