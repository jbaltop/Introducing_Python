# p392

from datetime import datetime as dt
import socket

server_address = ("localhost", 8080)
max_size = 4096

print("Starting the server")
print("Waiting for a client to call.")
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

data, client = server.recvfrom(max_size)
print(client, data)

if data == b"time":
    server.sendto(str(dt.now()).encode("utf-8"), client)

server.close()
