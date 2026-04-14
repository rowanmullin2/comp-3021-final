from abc import ABC,abstractmethod

class Observer(ABC):

	@abstractmethod
	def update(msg:str) -> None:
		"""
		Updates the observer with the given message.

		Args:
			msg (str): The message to be passed to the observer.

		"""
		pass