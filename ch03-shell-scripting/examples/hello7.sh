#!/bin/bash

NAME=${1:-$USER}
[[ -z "$NAME" ]] && NAME='Stranger'
echo "Hello, $NAME"
