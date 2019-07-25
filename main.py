from borrower import Borrower
from investor import Investor
from loan import Loan
from paymentFacade import PaymentFacade

# create Borrower
borrower1 = Borrower(balance=100000)
print('borrower1 is created!')


# List borrower1 loan Requests
print('List borrower1 loan Requests')
borrower1.checkMyLoanRequests()

# creat Loan instance
print('create loan')
loan1 = Loan()
print('loan1 created')

# test submitting request validation
print('test submitting request validation "invalid borrower instance"')
loan1.submitLoanRequest('borrower', amount=500000, installment_period=6)
print('test submitting request validation invalid amount')
loan1.submitLoanRequest(borrower1, amount=000, installment_period=6)
print('test submitting request validation invalid installment_period')
loan1.submitLoanRequest(borrower1, amount=5000, installment_period=-6)

# Submit valid request
print('Submit valid request')
loan1.submitLoanRequest(borrower1, amount=500000, installment_period=6)


# List borrower1 loan Requests
print('List borrower1 loan Requests')
borrower1.checkMyLoanRequests()

# Get loan1 details
print('Get loan1 details')
loan1.showLoanReqDetails()

# create Investors
print('create Investors')
investor1 = Investor(balance=2000000)
investor2 = Investor(balance=30000)
investor3 = Investor(balance=100)
print('investor1 identity{} investor2 identity{} investor3 identity{} are created'.format(investor1.identity,
                                                                                          investor2.identity, investor3.identity))

# Investors Submitting offers
print('investor1 submit valid offer')
loan1.submitLoanOffer(investor=investor1, interest=15)
print('investor2 submit valid offer')
loan1.submitLoanOffer(investor=investor2, interest=10)

# test submitting offer validation
print('investor3 submit invalid offer investor has no enough balance ')
loan1.submitLoanOffer(investor=investor3, interest=5)

# list loan1 offers
print('list loan1 offers')
loan1.showLoanOffers()

# Get a specific offerID
print('Get a specific offerID')
offerId = loan1.offers[0].id
print('selected offerID: {}'.format(offerId))

# Accept loan offer by offer Id
print('Accept loan offer by offer Id')
loan1.acceptLoanOffer(id=offerId)


# test submitting offer validation
print('test submitting offer validation try to submit an offer for an expired loan')
loan1.submitLoanOffer(investor=investor1, interest=3)

# test accepting offer validation
print('test submitting offer validation try to accept an already accepted offer again')
loan1.acceptLoanOffer(id=offerId)

transaction1 = PaymentFacade(loan=loan1)
transaction1.fundLoan()


print('PAYMENT SCHEDULE'+'-'*30)
transaction1.showPaymentSchedule()

print('First Transaction'+'-'*30)
transaction1.doMonthlyPayment()
print('showPaidSchedule '+'-'*30)
transaction1.showPaidSchedule()
print('showToPaySchedule '+'-'*30)
transaction1.showToPaySchedule()

print('Second Transaction'+'-'*30)
transaction1.doMonthlyPayment()
print('showPaidSchedule '+'-'*30)
transaction1.showPaidSchedule()
print('showToPaySchedule '+'-'*30)
transaction1.showToPaySchedule()

print('Third Transaction'+'-'*30)
transaction1.doMonthlyPayment()
print('showPaidSchedule '+'-'*30)
transaction1.showPaidSchedule()
print('showToPaySchedule '+'-'*30)
transaction1.showToPaySchedule()

print('Fourth Transaction'+'-'*30)
transaction1.doMonthlyPayment()
print('showPaidSchedule '+'-'*30)
transaction1.showPaidSchedule()
print('showToPaySchedule '+'-'*30)
transaction1.showToPaySchedule()

print('Fifth Transaction'+'-'*30)
transaction1.doMonthlyPayment()
print('showPaidSchedule '+'-'*30)
transaction1.showPaidSchedule()
print('showToPaySchedule '+'-'*30)
transaction1.showToPaySchedule()

print('Last Transaction'+'-'*30)
transaction1.doMonthlyPayment()
print('showPaidSchedule '+'-'*30)
transaction1.showPaidSchedule()
print('showToPaySchedule '+'-'*30)
transaction1.showToPaySchedule()

print(transaction1.getLoanStatus())

print(''' \n \n ---------------------------- summary ----------------------\n \n ''')

print('borrower1.balance: ', borrower1.balance)
print('investor1.balance:', investor1.balance)
print('borrower1.__dict__: ', borrower1.__dict__)
print('investor1.__dict__: ', investor1.__dict__)
print('loan1.__dict__: ', loan1.__dict__)
