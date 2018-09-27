# p125

number_thing = (number for number in range(1, 6))
print(type(number_thing))

for number in number_thing:
    print(number)

number_thing = (number for number in range(1, 6))
number_list = list(number_thing)
print(number_list)

try_again = list(number_thing)
print(try_again)
