from schema import Schema


class Option(Schema):
    """
    This class represents the table schema of Option table in database.
    """

    def __init__(self):
        self.name = 'Option'

        self.attributes = {
            'optionid': 'varchar(36)',
            'pollid': 'varchar(36)',
            'messageid': 'varchar(36)',
            'voteCount': 'integer',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'optionid',
        ]

        self.foreign_keys = {
            'pollid': 'Poll(pollid)',
            'messageid': 'Message(messageid)',
        }
