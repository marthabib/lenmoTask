import uuid


class Investor():

    def __init__(self, balance):
        self.__identity = uuid.uuid4()
        self.__balance = balance
        self.__outstanding = 0
        self.offers = []
        self.acceptedOffers = []

    @property
    def identity(self):
        return self.__identity

    @property
    def balance(self):
        return self.__balance

    @property
    def outstanding(self):
        return self.__outstanding

    def showMyOffers(self):
        print('showMyOffers ... in progress ...')
        return print('No Pending Offers \n' if (len(self.offers) == 0) else [offer.id for offer in self.offers])

    def showMyAcceptedOffers(self):
        print('showMyAcceptedOffers ... in progress ...')
        return print('No Accepted Offers \n' if (len(self.acceptedOffers) == 0) else [offer.id for offer in self.acceptedOffers])

    def pay(self, loanAmount, loanAmountWithInterest, lenmoProfiitAmount):
        self.__balance = self.__balance-loanAmount-lenmoProfiitAmount
        self.__outstanding = self.__outstanding + loanAmountWithInterest

    def gain(self, gainAmount):

        self.__balance = self.__balance + gainAmount
        self.__outstanding = self.__outstanding - gainAmount
