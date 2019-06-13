#!/bin/bash

WHOM="Who's on first" ./hello8.sh
WHOM="What's on second"
export WHOM
./hello8.sh
WHOM="I don't know's on third" ./hello8.sh
