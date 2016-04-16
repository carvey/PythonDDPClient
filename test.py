import time
from src.DDPClient import DDPClient
from random import randint

client = DDPClient('ws://localhost:3000/websocket')
response = client.receive()
print(response)

response = client.receive()
print(response)

# simulate receiving data and calling the JS sending the information to the server which calls a JS function
for i in range(randint(0, 10)):
    client.call("addPyData", randint(0, 100))
    time.sleep(.1)

response = client.receive()
print(response)
