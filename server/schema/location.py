from schema import Schema


class Location(Schema):
    """
    This class represents the table schema of Location table in database.
    """

    def __init__(self):
        self.name = 'Location'

        self.attributes = {
            'locationId': 'varchar(36)',
            'latitude': 'double precision',
            'longitude': 'double precision',
            'address': 'varchar(100)',
            'zip': 'integer',
        }

        self.primary_keys = [
            'locationId',
        ]

        self.foreign_keys = {

        }
