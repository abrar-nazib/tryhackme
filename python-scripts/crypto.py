#!/usr/bin/env python3

import sys

for elem in sys.argv:
    if(elem != sys.argv[0]):
        print(chr(int(elem)), end="")
print()
