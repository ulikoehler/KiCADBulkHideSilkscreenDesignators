#!/bin/sh
rm -rf build # remove old build directory
mkdir -p build/resources build/plugins
cp metadata.json build
cp *.py build/plugins
cp -r icon.png build/resources/
cd build && zip -r ../kicad-package.zip *