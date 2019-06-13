#!/usr/bin/env bash

if [[ $# -lt 1 ]]; then
    printf "Usage: %s NAME\n" $(basename $0)
    exit 1
fi

NAME=$1

if [[ $NAME == 'Lord Voldemort' ]]; then
    echo "Upon advice of my counsel, I respectfully refuse to say that name."
    exit 1
fi

echo "Hello, $1!"
