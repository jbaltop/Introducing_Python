import binascii
import struct

gif = binascii.unhexlify('47494638396101000100800000000000ffffff21f9' + '0401000000002c000000000100010000020144003b')
print(gif)

width, height = struct.unpack('<HH', gif[6:10])
print(width, height)
