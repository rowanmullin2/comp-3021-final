"""
    Client class
"""

__author__ = "Rowan Mullin"
__version__ = "1.0.0"

from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import date

class Client(Observer):
    """
        Represents a client with identifying information such as client 
        number, first name, last name, and email address.
    """

    def __init__(self, client_number:int, first_name:str, last_name:str,
        email_address: str):
        """
            Initializes a Client object with the given parameters.

            Args:
                client_number (int): The client number.
                first_name (str): The first name of the client.
                last_name (str): The last name of the client.
                email_address (str): The email address of the client.

            Raises:
                ValueError: If the client number, first name, or last 
                name is invalid.
                EmailNotValidError: If the email address is invalid.
        """

        # Validate that client_number is a numeric
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be numeric.")

        # Validate that first_name is not an empty string
        if len(first_name.strip()) > 0:
            self.__first_name = first_name.strip()
        else:
            raise ValueError("First Name must not be empty.")

        # Validate that last_name is not an empty string
        if len(last_name.strip()) > 0:
            self.__last_name = last_name.strip()
        else:
            raise ValueError("Last Name must not be empty.")

        # Validate Email
        try:
            validate_email(str(email_address),
                check_deliverability=False)
            self.__email_address = email_address
        except EmailNotValidError:
            # Fallback to default email if validation fails
            self.__email_address = "email@pixell-river.com"

    # Getter for client_number
    @property
    def client_number(self) -> int:
        """
			returns client_number:int
		"""
        return self.__client_number

    # Getter for first_name
    @property
    def first_name(self) -> str:
        """
			returns first_name:str
		"""
        return self.__first_name

    # Getter for last_name
    @property
    def last_name(self) -> str:
        """
			returns last_name:str
		"""
        return self.__last_name

    # Getter for email_address
    @property
    def email_address(self) -> str:
        """
			returns email_address:str
		"""
        return self.__email_address
    
    def update(self, message:str) -> None:
        """
        Sends a simulated email notification to the client's email 
        address.

        Args:
            message (str): The message to be included in the email 
            notification.

        Returns:
            None
        """
        
        simulate_send_email(
            self.__email_address,
            f"ALERT: Unusual Activity: {date.today()}",
            (f"Notification for {self.__client_number}: "+
            f"{self.__first_name} {self.__last_name}: {message}"))

    # String representation of the Client object
    def __str__(self) -> str:
        """
			returns str
		"""
        return (f"{self.__last_name}, {self.__first_name} "
                f"[{self.__client_number}] - {self.__email_address}")
    