from schema import Schema


class Identity(Schema):
    """
    This class represents the table schema of Identity table in database.
    """

    def __init__(self):
        self.name = 'Identity'

        self.attributes = {
            'userId': 'varchar(36)',
            'username': 'varchar(20) unique',
            'profileImageId': 'varchar(36)',
            'email': 'varchar(50)',
            'password': 'varchar(20)',
            'firstName': 'varchar(35)',
            'lastName': 'varchar(35)',
            'birthday': 'date',
            'facebook': 'varchar(50)',
            'status': 'varchar(20)',
            'deviceToken': 'varchar(50)',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'userId',
        ]

        self.foreign_keys = {
            'profileImageId': 'Image(imageId)',
        }
