"""
	chequing_account class
"""

__author__ = "Rowan Mullin"
__version__ = "1.0.0"

from patterns.strategy.overdraft_strategy import OverdraftStrategy
from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
	"""
		Represents a chequing account
	"""

	def __init__(self, account_number:int, client_number:int, balance:float, 
		date_created:date, overdraft_limit:float, overdraft_rate:float):
		"""
		Initializes a ChequingAccount object with the given parameters.

		Args:
			account_number (int): The account number.
			client_number (int): The client number.
			balance (float): The balance.
			date_created (date): The date the account was created.
			overdraft_limit (float): The overdraft limit.
			overdraft_rate (float): The overdraft rate.

		Raises:
			ValueError: If the account number, client number, balance, 
			or overdraft limit is invalid.
		"""
		super().__init__(account_number, client_number, balance, date_created)
		
		try:
			self.__overdraft_limit = float(overdraft_limit)
		except ValueError:
			self.__overdraft_limit = -100
		
		try:
			self.__overdraft_rate = float(overdraft_rate)
		except ValueError:
			self.__overdraft_rate = 0.05

		self.__strategy = OverdraftStrategy(self.__overdraft_limit,
			self.__overdraft_rate)

	def get_service_charges(self) -> float:
		"""
		Calculates the service charges for the account using the given
		strategy.

		Returns:
			float: The service charge amount.
		"""
		return self.__strategy.calculate_service_charges(self)
	
	def __str__(self) -> str:
		"""
			returns string representation of object
		"""
		return (super().__str__() +
			f"Overdraft Limit: ${self.__overdraft_limit:,.2f} Overdraft "+ 
			f"Rate: {self.__overdraft_rate*100:,.2f}"+
			"% Account Type: Chequing\n")
	