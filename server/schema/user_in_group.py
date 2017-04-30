from schema import Schema


class UserInGroup(Schema):
    """
    This class represents the table schema of UserInGroup table in database.
    """

    def __init__(self):
        self.name = "UserInGroup"
        self.attributes = {
            'groupid': 'varchar(36)',
            'userid': 'varchar(36)',
            'status': 'varchar(20)',
        }

        self.primary_keys = [
            'groupid',
            'userid',
        ]

        self.foreign_keys = {
            'groupid': 'LangGroup(groupid)',
            'userid': 'Identity(userid)',
        }