from schema import Schema


class Poll(Schema):
    """
    This class represents the table schema of Poll table in database.
    """

    def __init__(self):
        self.name = "Poll"
        self.attributes = {
            'pollId': 'varchar(36)',
            'status': 'varchar(20)',
        }

        self.primary_keys = [
            'pollId',
        ]

        self.foreign_keys = {
            'pollId': 'Message(messageId)',
        }