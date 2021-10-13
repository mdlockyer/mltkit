#!/bin/bash
PROJECT_DIR=$(dirname "$0")
BUILD_DIR=$PROJECT_DIR/build
rm -r $BUILD_DIR && echo Removed build directory: $BUILD_DIR
DIST_DIR=$PROJECT_DIR/dist
rm -r $DIST_DIR && echo Removed dist directory: $DIST_DIR
EGG_INFO_DIR=$PROJECT_DIR/*.egg-info
rm -r $EGG_INFO_DIR && echo Removed egg-info directories: $EGG_INFO_DIR
