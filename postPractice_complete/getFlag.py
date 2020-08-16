#!/usr/bin/env python3

import requests

data = {'username':'admin', 'password':'71urlkufpsdnlkadsf'}
resp = requests.post("http://165.227.106.113/post.php", data=data)

print(resp.text[4:27])