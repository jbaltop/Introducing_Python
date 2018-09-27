# p148

short_list = [1, 2, 3]
position = 5
# short_list[position] # IndexError

try:
    short_list[position]
except:
    print("Need a position between 0 and", len(short_list) - 1, " but got", position)
