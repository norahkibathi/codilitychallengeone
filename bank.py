import ipdb
import datetime
import math
def  solution (A,D):
          
      amount_balance = 0
      
      for i in range(len(A)):
          amount_balance  = A[i]
          date_x = D
          transaction_cost = 0
          start_date = datetime.date(2022,1,1)
          end_date = datetime.date(2023,12,1)
          month_date = math. int ("start_date - end_date")
          if A[i] < 0:
              if month_date == 3:
               transaction_cost = 100 * 12
               print (f"Card Payment", "and" transaction_cost)
                  
          if A[i] > 0:
               amount_balance +=  amount_balance - abs(5*12) 
               date_x = datetime.datetime() 
               print(f"Amount Balance",amount_balance , "the date of transaction is ", date_x)
              

ipdb.set_trace()               
