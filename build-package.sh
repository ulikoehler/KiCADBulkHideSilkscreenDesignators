#!/bin/sh
rm -rf build # remove old build directory
mkdir -p build/resources build/plugins
cp metadata.json build
cp *.py icon.png build/plugins
cp -r icon-64x64.png build/resources/icon.png
# cd build && zip -r ../kicad-package.zip *
cd build && winrar a -afzip ../kicad-package.zip *