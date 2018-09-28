# p392

import socket

server_address = ("localhost", 8080)
max_size = 4096

print("Starting the client")
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"time", server_address)
data, server = client.recvfrom(max_size)
print(server, data)
client.close()
