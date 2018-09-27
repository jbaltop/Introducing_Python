# p151


class UppercaseException(Exception):
    pass


words = ["eeenie", "meenie", "miny", "MO"]
for word in words:
    if word.isupper():
        raise UppercaseException(word)

# Traceback (most recent call last):
#   File "C:/Users/jbalt/hcrnbk6103/source/project_public/Introducing_Python/ch04/ex66_exception.py", line 11, in <module>
#     raise UppercaseException(word)
# __main__.UppercaseException: MO
