class Donor(object):
    """
    Maybe it would be a good idea to a make a simple donor class
    """
    def __init__(self, key : int, value : int):
        self.dictionary = {key : value}
        self.name = key
        self.donation = value

    def __str__(self):
        return f"{self.name} with a donation of {self.donation}"

    def getNameFromDonation(self, searchValue):
        for name, donation in self.dictionary.items():
            if donation == searchValue:
                return name
