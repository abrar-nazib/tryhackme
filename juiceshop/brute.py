#!/usr/bin/env python3

from email import header
import burptopy
import requests


burptopy_parser = burptopy.Burptopy("admin-bruteforce")
url, method, data, headers = burptopy_parser.parse_file()
headers = {"Cookie": headers["Cookie"]}
print(url)

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

r = requests.post(url=url, headers=headers,  proxies=proxies, verify=False)
print(headers)

print(r.text)
# print(headers)
