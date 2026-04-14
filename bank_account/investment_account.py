"""
	investment_account class
"""

__author__ = "Rowan Mullin"
__version__ = "1.0.0"

from patterns.strategy.management_fee_strategy import ManagementFeeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class InvestmentAccount(BankAccount):
	"""
		Represents a investment account
	"""

	TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

	def __init__(self, account_number:int, client_number:int, balance:float, 
		date_created:date, management_fee:float):
		"""
		Initializes an InvestmentAccount object with the given parameters.

		Args:
			account_number (int): The account number.
			client_number (int): The client number.
			balance (float): The balance.
			date_created (date): The date the account was created.
			management_fee (float): The management fee.

		Raises:
			ValueError: If the management fee is invalid.
		"""
		super().__init__(account_number, client_number, balance, date_created)
		
		try:
			self.__management_fee = float(management_fee)
		except:
			self.__management_fee = 2.55

		self.__strategy = ManagementFeeStrategy(self._date_created, 
			self.__management_fee)

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
		fee = (f"${self.__management_fee:,.2f}"
			if self._date_created >= InvestmentAccount.TEN_YEARS_AGO 
			else "Waived")
		return (super().__str__() + 
			f"Date Created: {self._date_created} Management Fee: "+
			f"{fee} Account Type: Investment\n")