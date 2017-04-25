from schema import Schema


class Vote(Schema):
    """
    This class represents the table schema of Vote table in database.
    """

    def __init__(self):
        self.name = "Vote";
        self.attributes = {
            'userid': 'varchar(36)',
            'optionid': 'varchar(36)',
            'pollid': 'varchar(36)',
        }

        self.primary_keys = [
            'userid',
            'optionid',
        ]

        self.foreign_keys = {
            'userid': 'Identity(userid)',
            'optionid': 'Option(optionid)',
            'pollid': 'Poll(pollid)',
        }