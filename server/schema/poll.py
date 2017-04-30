from schema import Schema


class Poll(Schema):
    """
    This class represents the table schema of Poll table in database.
    """

    def __init__(self):
        self.name = "Poll"
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