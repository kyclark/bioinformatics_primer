#!/bin/bash

set -u

GREETING=${1:-Hello}
NAME=${2:-Stranger}

echo "$GREETING, $NAME"
