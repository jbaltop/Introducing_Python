while True:
	value = input("Integer, please [q to quit]: ")
	if value == 'q':
		break
	number = int(value)
	if number %2 == 0:
		continue
	print(number, "squared is", number*number)
