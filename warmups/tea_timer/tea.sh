#!/usr/bin/env bash

TIME=${1:-120}
echo "Your tea will be ready in in $TIME seconds..."
sleep $TIME
echo 'Tea is ready!'
