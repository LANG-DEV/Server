from schema import Schema


class Option(Schema):
    """
    This class represents the table schema of Option table in database.
    """

    def __init__(self):
        self.name = 'Option'

        self.attributes = {
            'optionId': 'varchar(36)',
            'pollId': 'varchar(36)',
            'messageId': 'varchar(36)',
            'voteCount': 'integer',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'optionId',
        ]

        self.foreign_keys = {
            'pollId': 'Poll(pollId)',
            'messageId': 'Message(messageId)',
        }
