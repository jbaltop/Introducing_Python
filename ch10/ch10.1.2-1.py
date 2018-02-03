#!/usr/local/bin/python3

import os

print(os.path.exists('oops.txt'))
print(os.path.exists('./oops.txt'))
print(os.path.exists('waffles'))
print(os.path.exists('.'))
print(os.path.exists('..'))
