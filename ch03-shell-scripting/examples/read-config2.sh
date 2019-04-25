#!/bin/bash

CONFIG=${1:-config1.sh}
if [[ ! -f "$CONFIG" ]]; then
    echo "Bad config \"$CONFIG\""
    exit 1
fi

source $CONFIG
echo "$GREETING, $NAME!"
