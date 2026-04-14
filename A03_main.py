"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date
from client.client import Client

# 2. Create a Client object with data of your choice.
client1 = Client(1, "tim", "jenkins", "tj@rrc.ca")

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
account1 = ChequingAccount(100,1, 100, date.today(),10.0,1.0)
account2 = SavingsAccount(200,1,200,date.today(),10.0)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
account1.attach(client1)
account2.attach(client1)

# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
client2 = Client(2, "Mia", "Farly", "mf@rrc.ca")
account3 = SavingsAccount(201,2,400,date.today(),10.0)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
try:
	account1.deposit(10000)
	account1.withdraw(10060)
	account1.deposit(100)
	account2.deposit(10000)
	account2.withdraw(10160)
	account2.deposit(100)
	account3.deposit(10000)
	account3.withdraw(10360)
	account3.deposit(100)
except Exception as e:
	print(e)
