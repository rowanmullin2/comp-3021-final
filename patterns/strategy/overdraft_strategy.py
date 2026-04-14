from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):

	def __init__(self, overdraft_limit: float, overdraft_rate: float):
		"""
		Initializes an OverdraftStrategy object with the given 
		parameters.

		Args:
			overdraft_limit (float): The overdraft limit.
			overdraft_rate (float): The overdraft rate.

		Raises:
			ValueError: If the overdraft limit or rate is invalid.
		"""
		self.__overdraft_limit = overdraft_limit
		self.__overdraft_rate = overdraft_rate

	def calculate_service_charges(self, account: BankAccount) -> float:
		"""
		Calculates the service charges for the account.

		If the account balance is above or equal to the overdraft limit,
		the service charge is the base service charge.

		Otherwise, the service charge is the base service charge plus 
		the overdraft amount multiplied by the overdraft rate.

		Returns:
			float: The service charge amount.
		"""
		service_charge = 0

		if (account._BankAccount__balance >= self.__overdraft_limit):
			service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE
		elif (account._BankAccount__balance < self.__overdraft_limit):
			service_charge = (ServiceChargeStrategy.BASE_SERVICE_CHARGE + 
				(self.__overdraft_limit - account._BankAccount__balance)*
				self.__overdraft_rate)
		
		return round(service_charge,2)