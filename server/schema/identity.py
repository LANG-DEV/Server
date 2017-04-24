from schema import Schema


class Identity(Schema):
    """
    This class represents the table schema of Identity table in database.
    """

    def __init__(self):
        self.name = 'Identity'

        self.attributes = {
            'userid': 'varchar(36)',
            'username': 'varchar(20)',
            'email': 'varchar(50)',
            'password': 'varchar(20)',
            'firstname': 'varchar(35)',
            'lastname': 'varchar(35)',
            'birthday': 'date',
            'deviceToken': 'varchar(50)',
            'timeCreated': 'timestamp',
            'timeLastModified': 'timestamp',
        }

        self.primary_keys = [
            'userid',
        ]

        self.foreign_keys = {

        }
