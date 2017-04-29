from schema import Schema


class UserInGroup(Schema):
    """
    This class represents the table schema of UserInGroup table in database.
    """

    def __init__(self):
        self.name = "UserInGroup"
        self.attributes = {
            'groupId': 'varchar(36)',
            'userId': 'varchar(36)',
            'status': 'varchar(20)',
        }

        self.primary_keys = [
            'groupId',
            'userId',
        ]

        self.foreign_keys = {
            'groupId': 'LangGroup(groupId)',
            'userId': 'Identity(userId)',
        }