#!/bin/bash

echo "GIF8" > header

mkdir pngs

(dd if=header bs=1 count=4;cat unopenable.gif) >> flag.gif 2>/dev/null

convert flag.gif %0d.png

mv *.png pngs

cd pngs

for i in {1..4}; do convert ${i}.png -transparent white ${i}.png; done

for i in {0..4}; do convert -composite 0.png ${i}.png -gravity NorthEast 0.png; done

echo "ZmxhZ3tnMWZfb3JfajFmfQ==" | base64 -d 

echo ""

#cd ..
#rm -rf pngs