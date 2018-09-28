# p392

from datetime import datetime as dt
from xmlrpc.server import SimpleXMLRPCServer


def date_and_time(cmd):
    if cmd == "time":
        return dt.now()


print("Starting the server")
print("Waiting for a client to call.")
server = SimpleXMLRPCServer(("localhost", 8080))
server.register_function(date_and_time, "date_and_time")
server.serve_forever()
