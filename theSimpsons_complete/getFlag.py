#!/usr/bin/env python3

#on doind strings we got the following pseudo code
"""
Ahh! Realistically the Simpsons would use octal instead of decimal!
encoded = 152 162 152 145 162 167 150 172 153 162 145 170 141 162
key = chr(SolutionToDis(110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051))
key = key + key + chr(ord(key)-4)
print(DecodeDat(key=key,text=encoded))
"""

###by the pseudo code we have
key="110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051"
encoded="152 162 152 145 162 167 150 172 153 162 145 170 141 162"

###coverting to list 
encoded=encoded.split()
key=key.split()

###variables to convert the octal to string
keyString=""
encodedString=""

#converting the key to string
for x in key:
	keyString+=chr(int(x,8))

#converting the encoded value to string
for y in encoded:
	encodedString+=chr(int(y,8))

#gives the key as string
print("octal key to string={}".format(keyString)) 
##How much did Maggie originally cost? (Divided by 8, to the nearest integer, and then plus four)
##on googling i got the answer 847.63 
##so,
maggieCost=847.63

key=chr(round(maggieCost/8)+4) #n
key=key + key + chr(ord(key)-4) #by given
print("answer is",key)#which gives the key as "nnj"

#gives  the encoded octal in string format
print("octal encodedcontent to string={}".format(encodedString)) 

#now we have two strings on a key and a encoded text so one can easily guess it as a vigenere cipher
#you can use a online decoder or,


def decrypt(key, ciphertext):
    key_length = len(key)
    key_as_int = [ord(i) for i in key.upper()]
    ciphertext_int = [ord(i) for i in ciphertext.upper()]
    ans = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]+91)%91
        if value < 65:
            ans+=chr(value+65)
        else:
            ans+=chr(value)
    return ans.lower()

print(decrypt("nnj",encodedString))