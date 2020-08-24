#!/usr/bin/env python3

import requests

resp = requests.get("https://en.wikipedia.org/w/index.php?title=Flag&oldid=676540540")

flag = resp.text.split("<p>")
flag = flag[64].split("</p>")

print(flag[0])	


"""this problem actually don't require a script all you need to do is go to wikipedia
   search for the ip, press ctrl+f and search for "CTF" and you will found the flag"""