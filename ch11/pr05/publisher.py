# p392

import zmq
import string
from time import sleep

mammoth = """We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Parris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, the songs or glees
We could not sing, oh! queen of cheese.

We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
"""

host = "127.0.0.1"
port = 8080

print("Starting the server")
print("Waiting for a client to call")
context = zmq.Context()
server = context.socket(zmq.PUB)
server.bind("tcp://%s:%s" % (host, port))

sleep(1)

words = mammoth.split()
for word in words:
    word = word.strip(string.punctuation)
    data = word.encode("utf-8")
    if word.startswith(("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")):
        server.send_multipart([b"vowels", data])
    if len(word) == 5:
        server.send_multipart([b"five", data])
