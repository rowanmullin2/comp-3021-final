"""
Description: Unit tests for the Client class.
Author: Rowan Mullin
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from client.client import Client

class TestClient(unittest.TestCase):
    """
        Unit tests for the Client class.

        This test suite verifies the initialization and attribute 
        validation logic of the Client class. It checks for correct 
        assignment of valid values and ensures that invalid inputs raise
        appropriate exceptions. Additionally, it tests the string 
        representation of the Client object.

        Tested features:
            - Valid and invalid initialization of Client objects
            - Attribute accessors for client_number, first_name, 
              last_name, and email_address
            - Default email assignment when an invalid email is provided
            - String representation of Client instances
    """
  
    def setUp(self):
        # Arrange & Act used through out file
        self.example_data = [100,"Tim","Bugle","timB@rrc.ca"]
        self.example_client = Client(self.example_data[0],
                                     self.example_data[1],
                                     self.example_data[2],
                                     self.example_data[3])

    def test_init_valid(self):
        # Assert
        self.assertEqual(self.example_data[0],
                         self.example_client._Client__client_number)
        self.assertEqual(self.example_data[1],
                         self.example_client._Client__first_name)
        self.assertEqual(self.example_data[2],
                         self.example_client._Client__last_name)
        self.assertEqual(self.example_data[3],
                         self.example_client._Client__email_address)
    
    def test_init_invalid_client_number_raises_exception(self):
        # Arrange
        invalid_client_number = "0"
        # Act & Assert
        with self.assertRaises(ValueError):
            Client(invalid_client_number,self.example_data[1],
                    self.example_data[2],self.example_data[3])

    def test_init_invalid_first_name_raises_exception(self):
        # Arrange
        invalid_first_name = ""
        # Act & Assert
        with self.assertRaises(ValueError):
            Client(self.example_data[0],invalid_first_name,
                    self.example_data[2],self.example_data[3])

    def test_init_invalid_last_name_raises_exception(self):
        # Arrange
        invalid_last_name = ""
        # Act & Assert
        with self.assertRaises(ValueError):
            Client(self.example_data[0],self.example_data[1],
                    invalid_last_name,self.example_data[3])

    def test_init_invalid_email_address_raises_exception(self):
        # Arrange
        invalid_email_address = ""
        expected = "email@pixell-river.com"
        # Act
        client = Client(self.example_data[0],self.example_data[1],
                        self.example_data[2],invalid_email_address)
        # Assert
        self.assertEqual(expected, client._Client__email_address)

    def test_client_number_valid(self):
        # Arrange & Act & Assert
        self.assertEqual(self.example_data[0], 
                         self.example_client.client_number)

    def test_first_name_valid(self):
        # Arrange & Act & Assert
        self.assertEqual(self.example_data[1], 
                         self.example_client.first_name)

    def test_last_name_valid(self):
        # Arrange & Act & Assert
        self.assertEqual(self.example_data[2], 
                         self.example_client.last_name)

    def test_email_address_valid(self):
        # Arrange & Act & Assert
        self.assertEqual(self.example_data[3], 
                         self.example_client.email_address)
    
    def test_str_valid(self):
        # Arrange
        expected = (
                    f"{self.example_client._Client__last_name}, " 
                    f"{self.example_client._Client__first_name} "
                    f"[{self.example_client._Client__client_number}] - "
                    f"{self.example_client._Client__email_address}"
                   )
        # Act & Assert
        self.assertEqual(expected,str(self.example_client))
