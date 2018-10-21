# p392

import zmq

host = "127.0.0.1"
port = 8080
context = zmq.Context()
client = context.socket(zmq.SUB)
client.connect("tcp://%s:%s" % (host, port))
client.setsockopt(zmq.SUBSCRIBE, b"vowels")
client.setsockopt(zmq.SUBSCRIBE, b"five")
while True:
    topic, word = client.recv_multipart()
    print(topic, word)
