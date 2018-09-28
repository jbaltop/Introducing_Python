# p392

import xmlrpc.client

print("Starting the client")
proxy = xmlrpc.client.ServerProxy("http://localhost:8080/")
date_and_time = proxy.date_and_time("time")
print(date_and_time)
