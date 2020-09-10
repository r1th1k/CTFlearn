#!/usr/bin/env python


#creating a xor function to convert the hex value to a valid string using the key
def xor(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))

def helper(msgs):
    key = 'ALEXCTF{' #assigning the known part of the key
    max_len = max(map(len, msgs)) #determining the max length of the given hex
    while True: # iterating untill the key is found
        print key
        for i, msg in enumerate(msgs):
            print '%-2d' % i, xor(key, msg)
        if len(key) == max_len:
            break # if key found exit
        else:
        	val = raw_input("enter value: ") #if you can guess the next character of key enter the value
        	if val == "":
        		i = int(raw_input('\nline: ')) #enter the line to which u are trying to guess
        		c = raw_input('char: ') #enter the character
		        key += xor(msgs[i][len(key)], c) #xoring the hex value at the particular position using the character 	
        	else:
        		key+=val #just appending the value if it is known and continuing

with open('msg') as f:
    helper([x.strip().decode('hex') for x in f])
