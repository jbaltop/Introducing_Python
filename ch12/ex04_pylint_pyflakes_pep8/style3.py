# p402

"""usage
$ pylint style3.py
$ pyflakes style3.py
$ pycodestyle style3.py

pep8 has been renamed to pycodestyle (GitHub issue #466)
Use of the pep8 tool will be removed in a future release.
Please install and use `pycodestyle` instead."""

# """module docstring"""


def func():
    """function docstring. hi, mom!"""
    first = 1
    second = 2
    third = 3
    print(first)
    print(second)
    print(third)


if __name__ == "__main__":
    func()
