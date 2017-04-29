from schema import Schema


class Message(Schema):
    """
    This class represents the table schema of Message table in database.
    """

    def __init__(self):
        self.name = 'Message'

        self.attributes = {
            'messageId': 'varchar(36)',
            'chatRoomId': 'varchar(36)',
            'content': 'varchar(1000)',
            'type': 'varchar(15)',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'messageId',
        ]

        self.foreign_keys = {
            'chatRoomId': 'ChatRoom(chatRoomId)',
        }