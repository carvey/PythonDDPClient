from src.DDPClient import DDPClient

# client = DDPClient('ws://localhost:3000/websocket')
client = DDPClient('ws://www.charlesarvey.com/websocket')

response = client.receive()
print(response)

response = client.receive()
print(response)


client.call('disableGraphClear')
response = client.receive()
print(response)