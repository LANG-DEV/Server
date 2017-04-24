from schema import Schema


class Board(Schema):
    """
    This class represents the table schema of Board table in database.
    """

    def __init__(self):
        self.name = 'Board'

        self.attributes = {
            'boardid': 'varchar(36)',
            'groupid': 'varchar(36)',
            'locationid': 'varchar(36)',
            'time': 'timestamp with time zone',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'boardid',
        ]

        self.foreign_keys = {
            'groupid': 'Group(groupid)',
            'locationid': 'Location(locationid)',
        }