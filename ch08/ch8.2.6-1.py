#!/usr/local/bin/python3

# 보안되지 않은 parse
from xml.etree.ElementTree import parse
et = parse(xmlfile)

# 보안된 parse
from defusedxml.ElementTree import parse
et = parse(xmlfile)
