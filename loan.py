from offer import Offer
import datetime
import uuid
from borrower import Borrower


class Loan():

    def __init__(self):

        self.status = None
        self.borrower = None
        self.investor = None
        self.interest = None
        self.amount = None
        self.installment_period = None
        self.acceptedOffer = None
        self.loanAlreadyTaken = False
        self.reqSubmitted = False
        self.__identity = str(uuid.uuid4())
        self.time = str(datetime.datetime.now())
        self.offers = []

    @property
    def identity(self):
        return str(self.__identity)

    def getLoanStatus(self):
        return self.status

    def changeLoanStatus(self, status):
        self.status = status

    def __isValidRequest(self, borrower, amount, installment_period):

        if isinstance(borrower, Borrower) and amount > 0 and installment_period > 0 and not self.loanAlreadyTaken:
            return True
        else:
            return False

    def submitLoanRequest(self, borrower, amount, installment_period):

        print('submitLoanRequest ... in progress ...')
        if self.__isValidRequest(borrower, amount, installment_period):
            self.status = 'Requested'
            self.borrower = borrower
            self.borrower.loans.append(self)
            self.amount = amount
            self.installment_period = installment_period
            self.reqSubmitted = True
            return print('Thanks! your request has been successfully submitted. \n')
        else:
            return print('Sorrys! your request is invalid. \n')

    def showLoanReqDetails(self):

        print('showLoanReqDetails ... in progress ...')

        if self.reqSubmitted:
            return print({
                'amount': self.amount,
                'installment_period': self.installment_period,
                'submitted_at': self.time
            })
        else:
            return print('No available Loan requests \n')

    def __isValidOffer(self, investor, interest):

        isValid = False
        if self.loanAlreadyTaken:
            validationErr = (
                'Sorry Loan is already applied by another Investor! \n')

        elif investor.balance < self.amount:
            validationErr = ('Sorry you dont have enough credit! \n')

        else:
            isValid = True
            validationErr = None

        return {'isValid': isValid, 'validationErr': validationErr}

    def submitLoanOffer(self, investor, interest):

        print('submitLoanOffer ... in progress ...')

        validation = self.__isValidOffer(investor, interest)
        if validation['isValid']:
            offer = Offer(investor, interest, self)
            investor.offers.append(offer)
            self.offers.append(offer)
            return print('Thanks your offer is successfully submitted! \n')
        else:
            return print(validation['validationErr'])

    def showLoanOffers(self):

        print('showLoanOffers ... in progress ...')

        return print('Sorry no one submit offers yet! \n' if len(self.offers) == 0 else [(offer.id, offer.interest) for offer in self.offers])

    def __getOfferById(self, id):
        acceptedOffer = None
        for offer in self.offers:
            if offer.id == id:
                acceptedOffer = offer
        return acceptedOffer

    def acceptLoanOffer(self, id):

        print('acceptLoanOffer ... in progress ...')
        if self.loanAlreadyTaken:
            return print('Loan Offer already accepted and money already transfered! \n')
        acceptedOffer = self.__getOfferById(id)
        if acceptedOffer:
            self.loanAlreadyTaken = True
            self.acceptedOffer = acceptedOffer
            self.investor = acceptedOffer.investor
            self.interest = acceptedOffer.interest
            self.investor.acceptedOffers.append(acceptedOffer)
            self.status = 'Accepted'
            return print("Offer has been accepted successfully !\n")

        else:
            return print('Invalid offerID! \n')

    def showAcceptedOffer(self):
        if self.acceptedOffer:
            return print('accepted offer Id= {} accepted offer investor identity {} accepted offer interest {}'
                         .format(self.acceptedOffer.id, self.acceptedOffer.investor.identity, self.acceptedOffer.interest))
        else:
            print('no offer has been accepted yet!')
