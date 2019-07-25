# program shows the details of the loan

# will take the input values from user

from dateutil.relativedelta import relativedelta
from datetime import date, timedelta


# ---function for monthly loan amount calculation---


def monthly_loan(principal, interest_rate, duration):
    n = duration  # total number of months
    r = interest_rate/(100*12)  # interest per month
    # formula for compound interest applied on mothly payments.
    monthly_payment = principal*((r*((r+1)**n))/(((r+1)**n)-1))
    return monthly_payment

# ---funtion for remaining loan balance calculation---


def remaining_bal(principal, annual_interest_rate, duration, payments):
    r = annual_interest_rate/1200  # monthly interest rate
    m = r + 1
    n = duration  # duration in months

    # remaining balance using compound interest formula
    remaining = principal*(((m**n)-(m**payments))/((m**n)-1))
    return remaining


def createSchedule(principal, duration, interest_rate, monthly):

    schedule = []
    dates = [date.today() + relativedelta(months=i) for i in range(duration+1)]
    for x in range(1, duration+1):
        mon = x
        rem = remaining_bal(principal, interest_rate, duration, mon)
        schedule.append({"month": x, 'paymentdate': str(dates[x]), 'monthlypayment': monthly, "balanceRemaining": int(rem),
                         "totalPayments": int(monthly * mon)})
    return schedule
