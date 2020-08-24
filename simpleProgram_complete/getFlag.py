#!/usr/bin/env python3


with open("data.dat", "r") as file:
	lines=file.readlines()
	count = 0 #at first i tried to count from 1 but it didn't work you need to start counting from zero 
	for line in lines:
		 n0=line.count("0")
		 n1=line.count("1")

		 if n0%3==0 or n1%2==0:
		 	count+=1

print("flag is {}".format(count))
