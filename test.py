from src.DDPClient import DDPClient
from pprint import pprint
from random import randint

client = DDPClient('ws://localhost:3000/websocket')
response = client.receive()
print(response)

response = client.receive()
print(response)

# Test the connection with some ping/pong heartbeats
import time
# time.sleep(1)
for i in range(30):
    # client.ping(str(i))
    # response = client.receive()
    # print(response)
    client.call("addPyData", randint(0, 100))
    time.sleep(.1)



response = client.receive()
print(response)
