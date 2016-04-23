from src.DDPClient import DDPClient
from pprint import pprint
from random import randint

client = DDPClient('ws://localhost:3000/websocket')
response = client.receive()
print(response)

response = client.receive()
print(response)


import time
for i in range(25):
    client.call("addPyData", randint(0, 100))
    response = client.receive()
    pprint(response)
    time.sleep(.7)
