#!/bin/bash

SCRIPT_DIR=$(dirname $(readlink -f $0))
TARGET_DIR="$SCRIPT_DIR/test-coingecko-python"
if [ -d "$TARGET_DIR" ]; then
    find $TARGET_DIR -mindepth 1 -not -name '.gitkeep' -exec rm -rf {} +
fi
openapi-generator generate \
    -i $SCRIPT_DIR/coingecko-api.yml \
    -g python \
    -o $TARGET_DIR \
    -c $SCRIPT_DIR/openapi-config.json
