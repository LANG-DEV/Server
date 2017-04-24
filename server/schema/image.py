from schema import Schema


class Image(Schema):
    """
    This class represents the table schema of Image table in database.
    """

    def __init__(self):
        self.name = 'Image'

        self.attributes = {
            'imageid': 'varchar(36)',
            'endpoint': 'varchar(200)',
            'eventid': 'varchar(36)',
            'width': 'integer',
            'height': 'integer',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'imageid',
        ]

        self.foreign_keys = {
            'eventid': 'Event(eventid)',
        }