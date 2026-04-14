"""
	savings_account class
"""

__author__ = "Rowan Mullin"
__version__ = "1.0.0"

from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class SavingsAccount(BankAccount):
	"""
		Represents a savings account
	"""

	def __init__(self, account_number:int, client_number:int, balance:float, 
		date_created:date, minimum_balance:float):
		"""
		Initializes a SavingsAccount object with the given parameters.

		Args:
			account_number (int): The account number.
			client_number (int): The client number.
			balance (float): The balance.
			date_created (date): The date the account was created.
			minimum_balance (float): The minimum balance required to 
			avoid service charges.

		Raises:
			ValueError: If the minimum balance is invalid.
		"""
		super().__init__(account_number, client_number, balance, date_created)
		
		try:
			self.__minimum_balance = float(minimum_balance)
		except:
			self.__minimum_balance = 50

		self.__strategy = MinimumBalanceStrategy(self.__minimum_balance)

	def get_service_charges(self) -> float:
		"""
		Calculates the service charges for the account using the given
		strategy.

		Returns:
			float: The service charge amount.
		"""
		return self.__strategy.calculate_service_charges(self)
	
	def __str__(self):
		"""
		returns string representation of object
		"""
		return (super().__str__() + 
			f"Minimum Balance: ${self.__minimum_balance:,.2f} "+
			"Account Type: Savings\n")