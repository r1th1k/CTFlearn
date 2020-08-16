#!/bin/bash

binwalk --dd ".*" PurpleThing.jpeg 1>/dev/null

cd _*

tesseract 25795 flag 2>/dev/null

cat flag.txt