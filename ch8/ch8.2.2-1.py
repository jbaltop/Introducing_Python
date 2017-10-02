#!/usr/local/bin/python3

import xml.etree.ElementTree as et

tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
root.tag
