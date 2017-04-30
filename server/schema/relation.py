from schema import Schema


class Relation(Schema):
    """
    This class represents the table schema of Relation table in database.
    """

    def __init__(self):
        self.name = 'Relation'

        self.attributes = {
            'userId1': 'varchar(36)',
            'userId2': 'varchar(36)',
            'status': 'varchar(10)',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'userId1',
            'userId2',
        ]

        self.foreign_keys = {
            'userId1': 'Identity(userId)',
            'userId2': 'Identity(userId)',
        }
