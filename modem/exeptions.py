class InvalidVendor(Exception):
    def __init(self, value):
        self.parameter = value

    def __str__(self):
        return repr(self.parameter)
