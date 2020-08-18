#!/usr/bin/env python

given="41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D"
givenList=given.split()

flag=""
for i in givenList:
	flag+=chr(int(i,16))

print(flag)