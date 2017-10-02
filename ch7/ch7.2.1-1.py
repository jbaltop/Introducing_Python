#!/usr/local/bin/python3

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)
the_byte_array = bytearray(blist)
print(the_byte_array)

the_byte_array = bytearray(blist)
print(the_byte_array)
the_byte_array[1] = 127
print(the_byte_array)
