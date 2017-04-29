from schema import Schema


class ChatRoom(Schema):
    """
    This class represents the table schema of ChatRoom table in database.
    """

    def __init__(self):
        self.name = 'ChatRoom'

        self.attributes = {
            'chatRoomId': 'varchar(36)',
            'groupId': 'varchar(36)',
            'userCount': 'integer',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'chatRoomId',
        ]

        self.foreign_keys = {
            'groupId': 'LangGroup(groupId)',
        }
