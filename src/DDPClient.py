from websocket import create_connection
from .message import *


class DDPClient():

    def __init__(self, host):
        # open the websocket connection
        self.connection = create_connection(host)

        # init a connection message and connect to the host
        connect_msg = ConnectionMessage(version='1', support=['1'])
        self.send(connect_msg)

    def send(self, message):
        self.connection.send(message.serialize())

    def receive(self):
        response = self.connection.recv()
        return Message.resolve_message(response)

    def ping(self, id=""):
        ping_message = PingMessage(id=id)
        self.send(ping_message)

    def call(self, method, *args, **kwargs):
        message = MethodMessage(id=4, method=method)
        print('message :' + str(message))
        self.send(message)

