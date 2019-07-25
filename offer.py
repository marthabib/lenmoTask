import uuid


class Offer():

    def __init__(self, investor, interest, loan):
        self.__id = str(uuid.uuid4())
        self.interest = interest
        self.investor = investor
        self.loan = loan

    @property
    def id(self):
        return self.__id
