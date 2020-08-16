#!/usr/bin/env python3

import requests

header={'user-agent':'Sup3rS3cr3tAg3nt', 'referer':'awesomesauce.com'}
resp = requests.get("http://165.227.106.113/header.php", headers=header)

flag=resp.text

print(flag[19:53])