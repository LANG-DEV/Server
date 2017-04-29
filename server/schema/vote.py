from schema import Schema


class Vote(Schema):
    """
    This class represents the table schema of Vote table in database.
    """

    def __init__(self):
        self.name = "Vote";
        self.attributes = {
            'userId': 'varchar(36)',
            'optionId': 'varchar(36)',
            'pollId': 'varchar(36)',
        }

        self.primary_keys = [
            'userId',
            'optionId',
        ]

        self.foreign_keys = {
            'userId': 'Identity(userId)',
            'optionId': 'Option(optionId)',
            'pollId': 'Poll(pollId)',
        }