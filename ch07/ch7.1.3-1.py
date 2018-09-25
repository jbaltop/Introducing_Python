import re

result = re.match('You', 'Young Frankenstein')
print(result)

youpattern = re.compile('You')
result = youpattern.match('Young Frankenstein')
print(result)
