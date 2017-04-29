from schema import Schema


class Board(Schema):
    """
    This class represents the table schema of Board table in database.
    """

    def __init__(self):
        self.name = 'Board'

        self.attributes = {
            'boardId': 'varchar(36)',
            'groupId': 'varchar(36)',
            'locationId': 'varchar(36)',
            'time': 'timestamp with time zone',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'boardId',
        ]

        self.foreign_keys = {
            'groupId': 'LangGroup(groupId)',
            'locationId': 'Location(locationId)',
        }