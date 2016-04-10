from src.DDPClient import DDPClient

client = DDPClient('ws://localhost:3000/websocket')
response = client.receive()
print(response)

response = client.receive()
print(response)

# Test the connection with some ping/pong heartbeats
import time
time.sleep(1)
for i in range(10):
    client.ping(str(i))
    response = client.receive()
    print(response)
    time.sleep(2)
