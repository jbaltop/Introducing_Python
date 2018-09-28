# Introducing Python

Source code for the book "Introducing Python" by Bill Lubanovic.

## Prerequisites
* [python](https://www.python.org/)
* [sqlite tools](https://www.sqlite.org/)
* [memcached (not tested it yet)](https://memcached.org/)
* [redis](https://redis.io/)
* [apache (not tested it yet)](http://httpd.apache.org/)

## Setup

### Create Virtual Environment

On Linux and Mac (bash):

```
$ python3 -m venv env
```

On Windows (cmd):

```
> python -m venv env
```

### Activate Virtual Environment

On Linux and Mac:

```
$ source env/bin/activate
```

On Windows:

```
> env\Scripts\activate
```

### Install required packages

```
$ pip install -r requirements.txt
```

### Make output directory.

On Linux and Mac:

```
$ mkdir ch08/output ch10/output ch12/output
```

On Windows:

```
> md ch08\output ch10\output ch12\output
```

## References
* "처음 시작하는 파이썬" 빌 루바노빅 지음
* [official source code](http://download.hanbit.co.kr/exam/2239/)
* [official source code (github)](https://github.com/madscheme/introducing-python)

### Original book
* "Introducing Python" by Bill Lubanovic

## Abbreviations
* ch: chapter
* ex: example
* pr: problem

## Todo
Refer to `./TODO.txt`.
