#calcuting the bank balances from amount balance , and transaction that is a product of months
#A is an index representing the amount balance
#D represents the date
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
        end_date = datetime.date(2022, 12, 1)
        month_duration = (end_date - start_date).date
        month_duration = month_duration // 30  
# the  loop to calculate the monthly amounts when generating the loop it rember we have cash and payment system
        if A[i] < 0:
            if month_duration == 3:
               transaction_cost = 100 * 12
            print(f"Card Payment: {transaction_cost}")
        elif A[i] > 0:
            amount_balance += A[i] - abs(5 * 12)
            print(f"Amount Balance: {amount_balance} on {D[i].strftime('%Y-%m-%d')}")

#examples
A = [100, 100, 100, -10]
D = [datetime.date(2020, 12, 31), datetime.date(2020, 12, 22), datetime.date(2020, 12, 29), datetime.date(2020, 4, 1)]
solution(A, D)

ipdb.set_trace()
solution(A, D)
