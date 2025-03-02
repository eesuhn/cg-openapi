#!/bin/bash

SCRIPT_DIR=$(dirname $(readlink -f $0))
openapi-generator generate \
    -i $SCRIPT_DIR/coingecko-api.yml \
    -g python \
    -o $SCRIPT_DIR/test-coingecko-python
