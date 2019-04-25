#!/bin/bash

if [[ $# -ne 1 ]]; then
    printf "Usage: %s NAME\n" "$(basename "$0")"
    exit 1
fi

echo "Hello, $1!"
