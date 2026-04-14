from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):

	def __init__(self, date_created: date, management_fee: float):
		
		"""
		Initializes a ManagementFeeStrategy object with the given parameters.

		Args:
			date_created (date): The date the account was created.
			management_fee (float): The management fee.

		Raises:
			ValueError: If the management fee is invalid.
		"""
		self.__date_created = date_created
		self.__management_fee = management_fee
		self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

	def calculate_service_charges(self, account: BankAccount) -> float:
		"""
		Calculates the service charge for a given BankAccount.

		If the account was created more than 10 years ago, the service 
		charge is the base service charge plus the management fee.
		Otherwise, the service charge is the base service charge.

		Returns:
			float: The service charge amount.
		"""
		fee = (ServiceChargeStrategy.BASE_SERVICE_CHARGE + 
			self.__management_fee
			if self.__date_created >= account.TEN_YEARS_AGO 
			else ServiceChargeStrategy.BASE_SERVICE_CHARGE)
		return round(fee,2)