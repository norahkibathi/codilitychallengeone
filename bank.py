#calcuting the bank balances from amount balance , and transaction that is a product of months
import ipdb
import datetime
import math
#the function 
def solution(A, D):
    amount_balance = 0
#intializing the variables
    for i in range(len(A)):
        amount_balance = A[i]
        date_x = D[i]
        transaction_cost = 0

        start_date = datetime.date(2022, 1, 1)
        end_date = datetime.date(2023, 12, 1)
        month_duration = (end_date - start_date).date
        month_duration = month_duration // 30  
# the  loop to calculate the monthly amounts
        if A[i] < 0:
            if month_duration == 3:
                transaction_cost = 100 * 12
                print(f"Card Payment: {transaction_cost}")
        elif A[i] > 0:
            amount_balance += A[i] - abs(5 * 12)
            print(f"Amount Balance: {amount_balance} on {date_x.strftime('%Y-%m-%d')}")


A = [100, 100, 100, - 10]
D = [datetime.date(2020, 12, 31), datetime.date(2020, 12, 22), datetime.date(2020, 12, 29), datetime.date(2020, 4, 1)]
ipdb.set_trace()
solution(A, D)
