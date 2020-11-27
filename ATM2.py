import sys

#account balance 
account_balance = float(500.25)

#This is the print balance account function
def print_balance(balance):
  print('Your current balance is:')
  print(balance)

#This is the account deposit function with input(parameters)
def deposit(balance):
  deposit_amount = float(input("How much would you like to deposit today?\n"))
  balance = balance + deposit_amount
  print('Deposit was $%.2f, current balance is $%.2f' %(deposit_amount, balance))
  return balance

#This is the withdraw function
def withdrawal(balance):
  withdrawal_amount = float(input("How much would you like to withdrawal today?\n"))
  if withdrawal_amount > balance:
    print('$%.2f is greater than your account balance of $%.2f' %(withdrawal_amount, balance))
  else:
    balance = balance - withdrawal_amount
    print('Withdrawal amount was $%.2f, current balance is $%.2f' %(withdrawal_amount, balance))
    return balance
    
def print_summary():
    print('Thank you for banking with us today.')

#This line is were users would input what they would like to do as defined by variables, D, W, B and Q.
user_choice = input("What would you like to do?\n")

##The function below will return the correct output defined by the user
if user_choice == 'D':
  account_balance = deposit(account_balance)
elif user_choice == 'W':
  account_balance = withdrawal(account_balance)
elif user_choice == 'B':
    print_balance(account_balance)
elif user_choice == 'Q' :
   print_summary() 
  