#!/usr/bin/env python3

from Crypto.Util.number import inverse, long_to_bytes

#given
e = 3
c = 219878849218803628752496734037301843801487889344508611639028
n = 245841236512478852752909734912575581815967630033049838269083

p = 416064700201658306196320137931
q = 590872612825179551336102196593

phi = (p-1)*(q-1)

d = inverse(e, phi)

m = long_to_bytes(pow(c, d, n))

print(str(m)[2:23])

#if you need some help go and see my writeup for rsanoob +_+