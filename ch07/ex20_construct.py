# p225

from construct import Struct, Const, Int32ub

format = Struct(
    "signature" / Const(b"\x89PNG\r\n\x1a\n"),
    "length" / Int32ub,
    "type" / Const(b"IHDR"),
    "width" / Int32ub,
    "height" / Int32ub,
)

data = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR"
    + b"\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0"
)
result = format.parse(data)
print(result)
print(result.width, result.height)
