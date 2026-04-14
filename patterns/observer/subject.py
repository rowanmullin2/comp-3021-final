from abc import ABC,abstractmethod
from patterns.observer.observer import Observer

class Subject(ABC):

	def __init__(self):
		"""
		Initializes a Subject object, which is responsible for managing 
		a list of Observer objects.
		"""
		self._observers = []

	@abstractmethod
	def attach(observer:Observer) -> None:
		"""
		Attaches an observer to the subject. The observer will be 
		notified when the subject's state changes.
		
		Args:
			observer (Observer): The observer to be attached to the 
			subject.
		
		Raises:
			None
		"""
		pass

	@abstractmethod
	def detach(observer:Observer) -> None:
		"""
		Detaches an observer from the subject. The observer will no 
		longer be notified when the subject's state changes.
		
		Args:
			observer (Observer): The observer to be detached from the 
			subject.
		
		Raises:
			None
		"""
		pass

	@abstractmethod
	def notify(message:str) -> None:
		"""
		Notifies all the observers attached to the subject by passing 
		the given message.
		
		Args:
			message (str): The message to be passed to the observers.
		
		Raises:
			None
		"""
		pass