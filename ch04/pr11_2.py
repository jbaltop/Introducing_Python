# p152


class OopsException(Exception):
    pass


try:
    raise OopsException
except OopsException:
    print("Caught an oops")
