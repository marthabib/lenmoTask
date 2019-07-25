import uuid
print()


class Borrower():

    def __init__(self, balance):
        self.__identity = uuid.uuid4()
        self.__balance = balance
        self.__outstanding = 0
        self.loans = []

    @property
    def identity(self):
        return self.__identity

    @property
    def balance(self):
        return self.__balance

    @property
    def outstanding(self):
        return self.__outstanding

    def addLoan(self, loan):
        self.loans.append(loan)

    def checkMyLoanRequests(self):
        print('checkMyLoans ... in progress ...')
        return print('No Pending Loans \n' if (len(self.loans) == 0) else [loan.identity for loan in self.loans])

    def gain(self, loanAmount, loanAmountWithInterest):

        self.__balance = self.__balance+loanAmount
        self.__outstanding = self.__outstanding - loanAmountWithInterest

    def pay(self, payAmount):

        self.__balance = self.__balance - payAmount
        self.__outstanding = self.__outstanding + payAmount
