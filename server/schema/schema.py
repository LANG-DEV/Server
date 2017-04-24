class Schema:
    """
    This class is an abstract class to represent a table schema.
    """

    def __init__(self):
        self.attributes = {}
        self.primary_keys = []
        self.foreign_keys = {}
