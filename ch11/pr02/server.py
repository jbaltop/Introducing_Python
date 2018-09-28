# p392

from datetime import datetime as dt
import zmq

host = "127.0.0.1"
port = 8080

print("Starting the server")
print("Waiting for a client to call")
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://%s:%s" % (host, port))
while True:
    request_bytes = server.recv()
    request_str = request_bytes.decode("utf-8")
    print(request_str)
    if request_str == "time":
        reply_str = str(dt.now())
        reply_bytes = bytes(reply_str, "utf-8")
        server.send(reply_bytes)
