from src.DDPClient import DDPClient
from pprint import pprint

client = DDPClient('ws://localhost:3000/websocket')
response = client.receive()
print(response)

response = client.receive()
print(response)

# Test the connection with some ping/pong heartbeats
# import time
# time.sleep(1)
# for i in range(10):
#     client.ping(str(i))
#     response = client.receive()
#     print(response)
#     time.sleep(2)

client.call("addPyData", 15)

response = client.receive()
print(response)
