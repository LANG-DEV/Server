from schema import Schema


class Option(Schema):
    """
    
    """

    def __init__(self):
        self.name = 'Option'

        self.attributes = {
            'optionid': 'varchar(36)',
            'pollid': 'varchar(36)',
            'messageid': 'varchar(36)',
            'voteCount': 'integer',
        }

        self.primary_keys = [
            'optionid',
        ]

        self.foreign_keys = {
            'pollid': 'Poll(pollid)',
            'messageid': 'Message(messageid)',
        }
