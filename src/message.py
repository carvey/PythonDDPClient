import json
from collections import OrderedDict


class Message():

    def __init__(self, message_type, *args, **kwargs):
        self.msg = message_type
        self.fields = []

        for field in args:
            setattr(self, field, None)
            self.fields.append(field)

        self.fields.append('msg')

        for field, value in kwargs.items():
            if field not in self.fields:
                raise AttributeError(field)

            setattr(self, field, value)

    def __str__(self):
        return self.serialize()

    def serialize(self):
        field_values = OrderedDict()
        field_values['msg'] = self.msg

        for field in self.fields:
            field_values[field] = getattr(self, field)

        return json.dumps(field_values)

    @staticmethod
    def resolve_message(raw_message):
        message = json.loads(raw_message)
        message_type = message.get('msg', 'server_id')

        for subclass_cls in Message.__subclasses__():
            subclass = subclass_cls()
            if subclass.msg == message_type:
                return subclass_cls(**message)

        return message


class ConnectionMessage(Message):

    def __init__(self, *args, **kwargs):
        super(ConnectionMessage, self).__init__('connect', 'session', 'version', 'support', **kwargs)


class ConnectedMessage(Message):

    def __init__(self, *args, **kwargs):
        super(ConnectedMessage, self).__init__('connected', 'session', **kwargs)


class FailedMessage(Message):

    def __init__(self, *args, **kwargs):
        super(FailedMessage, self).__init__('failed', 'version', **kwargs)


class PingMessage(Message):

    def __init__(self, *args, **kwargs):
        super(PingMessage, self).__init__('ping', 'id', **kwargs)


class PongMessage(Message):

    def __init__(self, *args, **kwargs):
        super(PongMessage, self).__init__('pong', 'id', **kwargs)


class WelcomeMessage(Message):
    """
    Outdated message according the docs, but is still sent to start off every session for the time being
    """

    def __init__(self, *args, **kwargs):
        self.msg = 'server_id'
        self.server_id = kwargs.get('server_id', None)

    def serialize(self):
        return str({
            'server_id': self.server_id
        })


class MethodMessage(Message):

    def __init__(self, *args, **kwargs):
        super(MethodMessage, self).__init__('method', 'method', 'params', 'id', 'randomSeed', **kwargs)


class ResultMessage(Message):

    def __init__(self, *args, **kwargs):
        super(ResultMessage, self).__init__('result', 'id', 'error', 'result', **kwargs)


class UpdatedMessage(Message):

    def __init__(self, *args, **kwargs):
        super(UpdatedMessage, self).__init__('updated', 'methods', **kwargs)


