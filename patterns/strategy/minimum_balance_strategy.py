from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):

	def __init__(self, minimum_balance: float):
		
		"""
		Initializes a MinimumBalanceStrategy object with the given 
		parameters.

		Args:
			minimum_balance (float): The minimum balance required to 
			avoid service charges.

		Raises:
			ValueError: If the minimum balance is invalid.
		"""
		self.__minimum_balance = minimum_balance
		self.SERVICE_CHARGE_PREMIUM = 2.0

	def calculate_service_charges(self, account: BankAccount) -> float:
		"""
		Calculates the service charges for the account.

		If the account balance is above or equal to the minimum balance,
		the service charge is the base service charge.

		Otherwise, the service charge is the base service charge 
		multiplied by the service charge premium.

		Returns:
			float: The service charge amount.
		"""
		fee =  (ServiceChargeStrategy.BASE_SERVICE_CHARGE
			if account._BankAccount__balance >= self.__minimum_balance
			else ServiceChargeStrategy.BASE_SERVICE_CHARGE * 
			self.SERVICE_CHARGE_PREMIUM)
		return round(fee,2)