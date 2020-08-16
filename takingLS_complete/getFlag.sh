#note the below program will work only if the following are available
#python3
#wand module(pip3 install wand)
#tesseract

#!/bin/bash

unzip 'The Flag.zip' 1>/dev/null
cd 'The Flag'
cd .T*
pas=$(cat * | cut -c28-40)
echo "password for encrypted pdf:$pas"
cd ..
pdftk The\ Flag.pdf input_pw "Im The Flag" output flag.pdf 2>/dev/null

cat<<EOF>pdf2img.py

#!/usr/bin/env python3
from wand.image import Image as wi
pdfimg=wi(filename="flag.pdf", resolution=300)
pdfimg=pdfimg.convert("JPEG")
i=1
for imgpage in pdfimg.sequence:
	page=wi(image=imgpage)
	page.save(filename=str(i)+".jpg")
	i += 1

EOF

python3 pdf2img.py
tesseract 1.jpg flag 2>/dev/null
cat flag.txt 

echo "#########TESSERACT CAN'T ABLE TO IDENTIFY THE LAST WORD CORRECTLY IT IS COOl NOT COOI +_+############"

###########TESSERACT CAN'T ABLE TO IDENTIFY THE LAST WORD CORRECTLY IT IS COOl NOT COOI +_+################