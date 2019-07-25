from borrower import Borrower
from investor import Investor
from loan import Loan
from paymentFacade import PaymentFacade
from lenmoSingleton import Lenmo

borrower = Borrower(balance=100000)
investor = Investor(balance=2000000)
print('borrower balance =', borrower.balance)
print('investor balance =', investor.balance)
loan = Loan()
loan.submitLoanRequest(borrower=borrower, amount=500000, installment_period=6)

print('investor will check  loan request details submitted by borrower')

loan.showLoanReqDetails()

print('investor will submit loan offer')
loan.submitLoanOffer(investor, 15)

print('borrower will check all submitted offers by investors')
loan.showLoanOffers()

print('borrower will accept specific offer by offer id')
offerId = loan.offers[0].id
loan.acceptLoanOffer(id=offerId)

print('borrower will check all loan requests submitted by himself')
borrower.checkMyLoanRequests()

print('investor will check all loan offers submitted by himself')
investor.showMyOffers()

print('investor will check all the accepted  loan offers submitted by himself')
investor.showMyAcceptedOffers()

print('transaction will be done using Threading Lock to assure that only one transaction is on going at a particular moment')
transaction = PaymentFacade(loan)
transaction.fundLoan()

print('loan status changed to "Funded" and money is transfered to borrower successfully')
print('lenmo balance increased by 3 $ paid by Investor')
print('borrower balance =', borrower.balance)
print('borrower outstanding balance is =', borrower.outstanding)
print('investor balance =', investor.balance)
print('investor outstanding balance is =', investor.outstanding)


print('\n PAYMENT SCHEDULE'+'-'*30)
transaction.showPaymentSchedule()

print('\n First Transaction'+'-'*30)
transaction.doMonthlyPayment()
print('\n showPaidSchedule '+'-'*30)
transaction.showPaidSchedule()
print('\n showToPaySchedule '+'-'*30)
transaction.showToPaySchedule()

print('\n Second Transaction'+'-'*30)
transaction.doMonthlyPayment()
print('\n showPaidSchedule '+'-'*30)
transaction.showPaidSchedule()
print('\n showToPaySchedule '+'-'*30)
transaction.showToPaySchedule()

print('\n Third Transaction'+'-'*30)
transaction.doMonthlyPayment()
print('\n showPaidSchedule '+'-'*30)
transaction.showPaidSchedule()
print('\n showToPaySchedule '+'-'*30)
transaction.showToPaySchedule()

print('\n Fourth Transaction'+'-'*30)
transaction.doMonthlyPayment()
print('\n showPaidSchedule '+'-'*30)
transaction.showPaidSchedule()
print('\n showToPaySchedule '+'-'*30)
transaction.showToPaySchedule()

print('\n Fifth Transaction'+'-'*30)
transaction.doMonthlyPayment()
print('\n showPaidSchedule '+'-'*30)
transaction.showPaidSchedule()
print('\n showToPaySchedule '+'-'*30)
transaction.showToPaySchedule()

print('\n Last Transaction'+'-'*30)
transaction.doMonthlyPayment()
print('\n showPaidSchedule '+'-'*30)
transaction.showPaidSchedule()
print('\n showToPaySchedule '+'-'*30)
transaction.showToPaySchedule()

print(transaction.getLoanStatus())
