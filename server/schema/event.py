from schema import Schema


class Event(Schema):
    """
    This class represents the table schema of Event table in database.
    """

    def __init__(self):
        self.name = 'Event'

        self.attributes = {
            'eventid': 'varchar(36)',
            'chatroomid': 'varchar(36)',
            'boardid': 'varchar(36)',
            'capacity': 'integer',
            'userCount': 'integer',
            'name': 'varchar(20)',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'eventid',
        ]

        self.foreign_keys = {
            'chatroomid': 'ChatRoom(chatroomid)',
            'boardid': 'Board(boardid)',
        }
