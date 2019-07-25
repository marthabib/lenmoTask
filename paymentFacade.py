from paymentScheduleAndCalc import monthly_loan, createSchedule
from lenmoSingleton import Lenmo
import threading
import copy


class PaymentFacade():
    def __init__(self, loan):

        # check Loan status before creating the instance to assure that Loan is accepted!
        if loan.status != 'Accepted':
            return print('Sorry! you cannot do any payment transaction as the loan is not accepted yet!')

        self.__borrower = loan.borrower
        self.__loan = loan
        self.__investor = loan.acceptedOffer.investor
        self.__lenmo = Lenmo()
        self.__paymentSchedule = []
        self.__toPaySchedule = []
        self.__paidSchedule = []

    def getLoanStatus(self):
        return self.__loan.getLoanStatus()

    def __changeLoanStatus(self, status):
        self.__loan.changeLoanStatus(status)

    def __calculatMonthlyPayment(self):
        return monthly_loan(self.__loan.amount, self.__loan.interest, self.__loan.installment_period)

    def __calcTotalAmntWithInterest(self):
        try:
            return self.__calculatMonthlyPayment()*self.__loan.installment_period
        except Exception as err:
            print(err)
            return None

    def fundLoan(self):
        # Force synchronous threading on transaction method to avoid Async operation by applying the thread Lock using context manager
        # so that we assure only one transaction is in progress at a prticular moment
        with threading.Lock():
            if self.__loan.status != 'Funded':
                loanAmountwithInterest = self.__calcTotalAmntWithInterest()
                lenmoProfitAmount = self.__lenmo.profitAmount
                self.__investor.pay(loanAmount=self.__loan.amount,
                                    loanAmountWithInterest=loanAmountwithInterest, lenmoProfiitAmount=lenmoProfitAmount)
                self.__lenmo.gain()
                self.__borrower.gain(loanAmount=self.__loan.amount,
                                     loanAmountWithInterest=loanAmountwithInterest)
                self.__changeLoanStatus('Funded')
                self.__createPaymentSchedule()
                print('Loan has been Funded Successfully!')
            else:
                return print('Loan transaction already done before and loan status in Funded')

    def __createPaymentSchedule(self):

        # check if schedule already created before return it if not create new
        if len(self.__paymentSchedule) != 0:
            return self.__paymentSchedule

        # create new
        monthlyPay = self.__calculatMonthlyPayment()
        schedule = createSchedule(principal=self.__loan.amount, duration=self.__loan.installment_period,
                                  interest_rate=self.__loan.interest, monthly=monthlyPay)
        self.__paymentSchedule = schedule
        self.__toPaySchedule = schedule
        return schedule

    def __isValidToDoMonthlyPayment(self, monthlyPay):

        isValid = False
        if len(self.__toPaySchedule) == 0:
            error = 'no pending payment!'
        elif self.__borrower.balance < monthlyPay:
            error = 'Borrower do not have enough ceredit for thistransaction'
        else:
            isValid = True
            error = None
        return {'isValid': isValid, 'error': error}

    def doMonthlyPayment(self):

        monthlyPay = self.__calculatMonthlyPayment()
        validation = self.__isValidToDoMonthlyPayment(monthlyPay)
        if validation['isValid']:
            self.__borrower.pay(payAmount=monthlyPay)
            self.__investor.gain(gainAmount=monthlyPay)
            self.__paidSchedule.append(self.__toPaySchedule[0])

            del self.__toPaySchedule[0]
            print('Monthly payment done Successfully!')
            if len(self.__toPaySchedule) == 0:
                self.__changeLoanStatus('Completed')
        else:
            return print(validation['error'])

    def showPaymentSchedule(self):

        [print(x)
         for x in self.__paymentSchedule if len(self.__paymentSchedule) > 0]

    def showToPaySchedule(self):

        [print(x)
         for x in self.__toPaySchedule if len(self.__toPaySchedule) > 0]

    def showPaidSchedule(self):

        [print(x) for x in self.__paidSchedule if len(self.__paidSchedule) > 0]
