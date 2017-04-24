from schema import Schema


class ChatRoom(Schema):
    """
    This class represents the table schema of ChatRoom table in database.
    """

    def __init__(self):
        self.name = 'ChatRoom'

        self.attributes = {
            'chatroomid': 'varchar(36)',
            'groupid': 'varchar(36)',
            'userCount': 'integer',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'chatroomid',
        ]

        self.foreign_keys = {
            'groupid': 'Group(groupid)',
        }
