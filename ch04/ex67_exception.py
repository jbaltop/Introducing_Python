# p151


class OopsException(Exception):
    pass


try:
    raise OopsException("panic")
except OopsException as exc:
    print(exc)
