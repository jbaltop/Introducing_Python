# unsecure parse
from xml.etree.ElementTree import parse
et = parse(xmlfile)

# secure parse
from defusedxml.ElementTree import parse
et = parse(xmlfile)
