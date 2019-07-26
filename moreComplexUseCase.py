from borrower import Borrower
from investor import Investor
from loan import Loan
from paymentFacade import PaymentFacade
from lenmoSingleton import Lenmo

borrower1 = Borrower(balance=100000)
borrower2 = Borrower(balance=200000)
borrower3 = Borrower(balance=3000)
investor1 = Investor(balance=2000000)
investor2 = Investor(balance=1000000)
investor3 = Investor(balance=2000)
loan1 = Loan()
loan2 = Loan()
loan3 = Loan()

print('investor show loans requests before submitting any requests by the borrowers!')
loan1.showLoanReqDetails()

print('borrowers will submit requests  ')
loan1.submitLoanRequest(
    borrower=borrower1, amount=500000, installment_period=12)
loan2.submitLoanRequest(
    borrower=borrower2, amount=1000000, installment_period=9)

loan3.submitLoanRequest(borrower=borrower3, amount=1000, installment_period=6)


print('investor show loans request details!')
loan1.showLoanReqDetails()
loan2.showLoanReqDetails()
loan3.showLoanReqDetails()

print('\n investor1 will submit an offer to loan1 and loan2 ')
loan1.submitLoanOffer(investor=investor1, interest=15)
loan2.submitLoanOffer(investor=investor1, interest=15)

print('\n investor2 will submit an offer to loan1 and loan2 ')
loan1.submitLoanOffer(investor=investor2, interest=10)
loan2.submitLoanOffer(investor=investor2, interest=10)


print('\n investor 3 will try to submit offer but dont have enough credit for loan 2 ')
loan2.submitLoanOffer(investor=investor3, interest=10)
print('\n investor3 will successfully submit an offer to loan3 ')
loan3.submitLoanOffer(investor=investor3, interest=10)

print('\n borrower will check the available offers for thier requests ')
print('\n show loan 1 requests ')
loan1.showLoanOffers()
print('\n show loan 2 requests ')
loan2.showLoanOffers()
print('\n show loan 3 requests ')
loan3.showLoanOffers()

print('\n each borrower will accept the offer with lowest interest')

loan1bestOfferId = loan1.offers[1].id
print(loan1bestOfferId)
loan1.acceptLoanOffer(id=loan1bestOfferId)

loan2bestOfferId = loan2.offers[1].id
loan2.acceptLoanOffer(id=loan2bestOfferId)

loan3bestOfferId = loan3.offers[0].id
loan3.acceptLoanOffer(id=loan3bestOfferId)


print('\n investor1 will try to submit new offers but borrowers alread accepted another offers.')
loan1.submitLoanOffer(investor=investor1, interest=8)
loan2.submitLoanOffer(investor=investor1, interest=5)

print('creat transactions and fund loans')
transaction1 = PaymentFacade(loan1)
transaction2 = PaymentFacade(loan2)
transaction3 = PaymentFacade(loan3)
print('lenmo balance: ', Lenmo().balance)
transaction1.fundLoan()
print('lenmo balance: ', Lenmo().balance)
transaction2.fundLoan()
print('lenmo balance: ', Lenmo().balance)
transaction3.fundLoan()
print('lenmo balance: ', Lenmo().balance)


print('now we will show loan1 request details and loan1 accepted offer details and loan1 schedule')
loan1.showLoanReqDetails()
loan1.showAcceptedOffer()
print('\n loan 1 PAYMENT SCHEDULE'+'-'*30)
transaction1.showPaymentSchedule()

print('now we will show loan2 request details and loan2 accepted offer details and loan2 schedule')
loan2.showLoanReqDetails()
loan2.showAcceptedOffer()
print('\n loan 2 PAYMENT SCHEDULE'+'-'*30)
transaction2.showPaymentSchedule()

print('now we will show loan3 request details and loan3 accepted offer details and loan3 schedule')
loan3.showLoanReqDetails()
loan3.showAcceptedOffer()
print('\n loan 3 PAYMENT SCHEDULE'+'-'*30)
transaction3.showPaymentSchedule()

print('lenmo balance: ', Lenmo().balance)
print('borrower1 balance =', borrower1.balance)
print('borrower1 outstanding balance is =', borrower1.outstanding)
print('borrower2 balance =', borrower2.balance)
print('borrower2 outstanding balance is =', borrower2.outstanding)
print('borrower3 balance =', borrower3.balance)
print('borrower3 outstanding balance is =', borrower3.outstanding)
print('investor1 balance =', investor1.balance)
print('investor1 outstanding balance is =', investor1.outstanding)
print('investor2 balance =', investor2.balance)
print('investor2 outstanding balance is =', investor2.outstanding)
print('investor3 balance =', investor3.balance)
print('investor3 outstanding balance is =', investor3.outstanding)


print('borrowers will do payments ')
for x in range(13):
    transaction1.doMonthlyPayment()
for x in range(10):
    transaction2.doMonthlyPayment()
for x in range(7):
    transaction3.doMonthlyPayment()

print('lenmo balance: ', Lenmo().balance)
print('borrower1 balance =', borrower1.balance)
print('borrower1 outstanding balance is =', int(borrower1.outstanding))
print('borrower2 balance =', borrower2.balance)
print('borrower2 outstanding balance is =', int(borrower2.outstanding))
print('borrower3 balance =', borrower3.balance)
print('borrower3 outstanding balance is =', int(borrower3.outstanding))
print('investor1 balance =', investor1.balance)
print('investor1 outstanding balance is =', int(investor1.outstanding))
print('investor2 balance =', investor2.balance)
print('investor2 outstanding balance is =', int(investor2.outstanding))
print('investor3 balance =', investor3.balance)
print('investor3 outstanding balance is =', int(investor3.outstanding))
