from schema import Schema


class Image(Schema):
    """
    This class represents the table schema of Image table in database.
    """

    def __init__(self):
        self.name = 'Image'

        self.attributes = {
            'imageId': 'varchar(36)',
            'endpoint': 'varchar(200)',
            'width': 'integer',
            'height': 'integer',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'imageId',
        ]

        self.foreign_keys = {
            'imageId': 'LangGroup(groupId)',
        }