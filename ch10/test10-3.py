import time

fin = open('today.txt', 'rt')
today_string = fin.read()
fin.close()

fmt = "%Y-%m-%d\n"
print(time.strptime(today_string, fmt))
