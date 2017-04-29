from schema import Schema


class Group(Schema):
    """
    This class represents the table schema of Event table in database.
    """

    def __init__(self):
        self.name = 'LangGroup'

        self.attributes = {
            'groupId': 'varchar(36)',
            'chatRoomId': 'varchar(36)',
            'boardId': 'varchar(36)',
            'capacity': 'integer',
            'userCount': 'integer',
            'name': 'varchar(20)',
            'invitationCode': 'varchar(6)',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'groupId',
        ]

        self.foreign_keys = {
            'chatRoomId': 'ChatRoom(chatRoomId)',
            'boardId': 'Board(boardId)',
        }
