from schema import Schema


class Group(Schema):
    """
    This class represents the table schema of Event table in database.
    """

    def __init__(self):
        self.name = 'Group'

        self.attributes = {
            'groupid': 'varchar(36)',
            'chatroomid': 'varchar(36)',
            'boardid': 'varchar(36)',
            'capacity': 'integer',
            'userCount': 'integer',
            'name': 'varchar(20)',
            'invitationCode': 'varchar(6)',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'groupid',
        ]

        self.foreign_keys = {
            'chatroomid': 'ChatRoom(chatroomid)',
            'boardid': 'Board(boardid)',
        }
