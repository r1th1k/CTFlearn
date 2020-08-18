#!/usr/bin/env python3

import subprocess
import base64

subprocess.call("cp flag.txt answer.txt", shell=True)

i=1
while i<=50: #I tested using while true statement and found that after 50 times decodind the flag is obtained
	f = open("answer.txt", "rb") 
	dat = f.read()
	val = base64.b64decode(dat)
	q = open("answer.txt", "wb")
	q.write(val)
	#print(i)
	i+=1


subprocess.call("cat answer.txt", shell=True)
print("\n")