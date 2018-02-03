#!/usr/local/bin/python3

import os

os.remove('oops.txt')
print(os.path.exists('oops.txt'))
