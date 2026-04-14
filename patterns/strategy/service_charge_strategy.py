from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
	
	BASE_SERVICE_CHARGE = 0.5

	@abstractmethod
	def calculate_service_charges(account: BankAccount) -> float:
		"""
		Calculates the service charge for a given BankAccount.

		Args:
			account (BankAccount): The BankAccount for which the 
			service charge should be calculated.

		Returns:
			float: The service charge amount.
		"""
		pass

