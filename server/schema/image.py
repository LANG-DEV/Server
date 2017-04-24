from schema import Schema


class Image(Schema):
    """
    
    """

    def __init__(self):
        self.name = 'Image'

        self.attributes = {
            'imageid': 'varchar(36)',
            'endpoint': 'varchar(200)',
            'eventid': 'varchar(36)',
        }

        self.primary_keys = [
            'imageid',
        ]

        self.foreign_keys = {
            'eventid': 'Event(eventid)',
        }