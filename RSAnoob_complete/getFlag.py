#!/usr/bin/env python3

from Crypto.Util.number import inverse, long_to_bytes

#given:
e = 1
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083

#use factordb to find the two prime numbers
p = 416064700201658306196320137931
q = 590872612825179551336102196593

#calculate phi 
phi = (p-1)*(q-1)

#calculate the decrypter val
d = inverse(e, phi)

#decrypt the text
m = long_to_bytes(pow(c, d, n))

print(str(m)[2:25])