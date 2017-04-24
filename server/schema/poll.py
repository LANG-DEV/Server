from schema import Schema


class poll(Schema):
    """
    This class represents the table schema of Poll table in database.
    """

    def __init__(self):
        self.attributes = {
            'pollid': 'varchar(36)',
            'status': 'varchar(20)',
        }

        self.primary_keys = [
            'pollid',
        ]

        self.foreign_keys = {
            'pollid': 'Message(messageid)',
        }