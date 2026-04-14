"""
	BankAccount class
"""

__author__ = "Rowan Mullin"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer

class BankAccount(Subject, ABC):
	"""
		Represents a bank account
	"""

	LARGE_TRANSACTION_THRESHOLD = 9999.99
	LOW_BALANCE_LEVEL = 50.0

	def __init__(self, account_number:int, client_number:int, 
		balance:float, date_created:date):
		"""
		Initializes a BankAccount object with the given parameters.

		Args:
			account_number (int): The account number.
			client_number (int): The client number.
			balance (float): The balance.
			date_created (date): The date the account was created.

		Raises:
			ValueError: If the account number, client number, or balance is invalid.
		"""
		
		super().__init__()

		# Validate that account_number is a numeric
		if isinstance(account_number, int):
			self.__account_number = account_number
		else:
			raise ValueError("Account Number must be numeric.")
	
		# Validate that client_number is a numeric
		if isinstance(client_number, int):
			self.__client_number = client_number
		else:
			raise ValueError("Client Number must be numeric.")
	
		# Validate that balance can be casted to a float
		try:
			self.__balance = float(balance)
		except Exception:
			self.__balance = 0

		# Validate that date_created is a date
		if isinstance(date_created, date):
			self._date_created = date_created
		else:
			self._date_created = date.today()
	
	@property
	def account_number(self) -> int:
		"""
			returns account_number:int
		"""
		return self.__account_number
	
	@property
	def client_number(self) -> int:
		"""
			returns client_number:int
		"""
		return self.__client_number
	
	@property
	def balance(self) -> float:
		"""
			returns balance:float
		"""
		return self.__balance
	
	def update_balance(self,amount:float) -> None:
		"""
		Updates the balance of the account by the given amount.

		Args:
			amount (float): The amount to add to the balance.

		Raises:
			ValueError: If the amount is not a positive numeric value.

		Notes:
			Will trigger a low balance warning if the resulting balance is below
			the low balance threshold.
			Will trigger a large transaction warning if the amount is above the
			large transaction threshold.
		"""
		if self.__balance < BankAccount.LOW_BALANCE_LEVEL:
			self.notify(f"Low balance warning {self.__balance:,.2f}: "+
				f"on account {self.__account_number}.")
			
		if amount > BankAccount.LARGE_TRANSACTION_THRESHOLD:
			self.notify(f"Large transaction {amount:,.2f}: on account "+
				f"{self.account_number}.")

		if isinstance(amount, (float,int)):
			self.__balance += amount

	def deposit(self, amount:float) -> None:
		"""
		Deposits the given amount into the account.

		Args:
			amount (float): The amount to deposit.

		Raises:
			ValueError: If the amount is not a positive numeric value.
		"""
		# Validate that amount is a numeric
		if not isinstance(amount, (float,int)):
			raise ValueError(f"Deposit amount: {amount} must be numeric.")
		# Validate that amount is a positive
		elif amount <= 0:
			raise ValueError(f"Deposit amount: ${amount:,.2f} must " 
							 "be positive.")
		# Looks good! pass to update_balance
		else: 
			self.update_balance(amount)

	def withdraw(self, amount:float) -> None:
		"""
		Withdraws the given amount from the account.

		Args:
			amount (float): The amount to withdraw.

		Raises:
			ValueError: If the amount is not a positive numeric value.
			ValueError: If the amount exceeds the account balance.
		"""
		# Validate that amount is a numeric
		if not isinstance(amount, (float,int)):
			raise ValueError(f"Withdraw amount: {amount} must be numeric.")
		# Validate that amount is a positive
		elif amount <= 0:
			raise ValueError(f"Withdraw amount: ${amount:,.2f} must "+
							 "be positive.")
		# Validate that amount is below the account's total
		elif amount > self.__balance:
			raise ValueError(f"Withdraw amount: {amount:,.2f} must not "+ 
							 "exceed the account balance: "+
							 f"{self.__balance:,.2f}.")
		# Looks good! pass to update_balance
		else: 
			self.update_balance(-amount)

	@abstractmethod
	def get_service_charges(self) -> float:
		"""
		Returns the service charge amount for the account.

		Abstract method, requires implementation from subclasses.

		Returns:
			float: The service charge amount.
		"""
		pass

	def attach(self, observer: Observer) -> None:
		"""
		Attaches an observer to the subject. The observer will be 
		notified when the subject's state changes.

		Args:
			observer (Observer): The observer to be attached to the 
			subject.

		Raises:
			None
		"""
		self._observers.append(observer)
	
	def detach(self, observer:Observer) -> None:
		"""
		Detaches an observer from the subject. The observer will no 
		longer be notified when the subject's state changes.
		
		Args:
			observer (Observer): The observer to be detached from the 
			subject.
		
		Raises:
			None
		"""
		if observer in self._observers:
			self._observers.remove(observer)
	
	def notify(self, message:str) -> None:
		"""
		Notifies all the observers attached to the subject by passing 
		the given message.

		Args:
			message (str): The message to be passed to the observers.

		Raises:
			None
		"""
		for observer in self._observers:
			observer.update(message)

	def __str__(self) -> str:
		"""
			returns string representation of object
		"""
		return ("Account Number: "
				f"{self._BankAccount__account_number} "
				"Balance: "
				f"${self._BankAccount__balance:,.2f}\n")
