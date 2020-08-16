#!/bin/bash 

unzip *.zip 1>/dev/null
cd gitIsGood
cd .git
git show 195dd65b9f5130d5f8a435c5995159d4d760741b | tail -1 | cut -c2-