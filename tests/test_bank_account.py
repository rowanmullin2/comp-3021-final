"""
Description: Unit tests for the BankAccount class.
Author: Rowan Mullin
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
"""
import unittest
from bank_account.bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
        # Arrange & Act used through out file
        self.example_data = [100,100,100.00]
        self.example_bank_account = BankAccount(self.example_data[0],
                                     self.example_data[1],
                                     self.example_data[2],)

    def test_init_valid(self):
        # Assert
        self.assertEqual(self.example_data[0],
                        self.example_bank_account._BankAccount__account_number)
        self.assertEqual(self.example_data[1],
                         self.example_bank_account._BankAccount__client_number)
        self.assertEqual(self.example_data[2],
                         self.example_bank_account._BankAccount__balance)
        
    def test_init_invalid_account_number_raises_exception(self):
        # Arrange
        invalid_account_number = "0"
        # Act & Assert
        with self.assertRaises(ValueError):
            BankAccount(invalid_account_number,self.example_data[1],
                        self.example_data[2])
        
    def test_init_invalid_client_number_raises_exception(self):
        # Arrange
        invalid_client_number = "0"
        # Act & Assert
        with self.assertRaises(ValueError):
            BankAccount(self.example_data[0],invalid_client_number,
                        self.example_data[2])
        
    def test_init_invalid_balance_raises_exception(self):
        # Arrange
        invalid_balance = "0"
        # Act 
        empty_balance_account = BankAccount(self.example_data[0],
                                            self.example_data[1],
                                            invalid_balance)
        # Assert
        self.assertEqual(0.0, empty_balance_account._BankAccount__balance)

    def test_account_number_valid(self):
        # Arrange & Act & Assert
        self.assertEqual(self.example_data[0], 
                         self.example_bank_account.account_number)  

    def test_client_number_valid(self):
        # Arrange & Act & Assert
        self.assertEqual(self.example_data[1], 
                         self.example_bank_account.client_number)  

    def test_balance_valid(self):
        # Arrange & Act & Assert
        self.assertEqual(self.example_data[2], 
                         self.example_bank_account.balance)  

    def test_update_balance_valid_positive_balance(self):
        # Arrange
        amount = 1
        
        # Act
        self.example_bank_account.update_balance(amount)

        # Assert
        self.assertEqual(101.00,
                         self.example_bank_account._BankAccount__balance)

    def test_update_balance_valid_negative_balance(self):
        # Arrange
        amount = -1
        
        # Act
        self.example_bank_account.update_balance(amount)

        # Assert
        self.assertEqual(99.00,
                         self.example_bank_account._BankAccount__balance)

    def test_update_balance_invalid_balance(self):
        # Arrange
        amount = "1"
        
        # Act
        self.example_bank_account.update_balance(amount)

        # Assert
        self.assertEqual(100.0,
                         self.example_bank_account._BankAccount__balance)

    def test_deposit_valid(self):
        # Arrange
        valid_amount = 1

        # Actual
        self.example_bank_account.deposit(valid_amount)

        # Assert
        self.assertEqual(101.00,
                         self.example_bank_account._BankAccount__balance)
    
    def test_deposit_invalid_amount_raises_exception(self):
        # Arrange
        invalid_amount = -1

        # Actual & Assert
        with self.assertRaises(ValueError):
            self.example_bank_account.deposit(invalid_amount)

    def test_withdraw_valid(self):
        # Arrange
        valid_amount = 1

        # Actual
        self.example_bank_account.withdraw(valid_amount)

        # Assert
        self.assertEqual(99.00,
                         self.example_bank_account._BankAccount__balance)
    
    def test_withdraw_invalid_amount_raises_exception(self):
        # Arrange
        invalid_amount = -1

        # Actual & Assert
        with self.assertRaises(ValueError):
            self.example_bank_account.withdraw(invalid_amount)
    
    def test_withdraw_invalid_exceed_amount_raises_exception(self):
        # Arrange
        invalid_amount = 101

        # Actual & Assert
        with self.assertRaises(ValueError):
            self.example_bank_account.withdraw(invalid_amount)

    def test_str_valid(self):
        # Arrange
        expected = (
                "Account Number: "
                f"{self.example_bank_account._BankAccount__account_number} "
                "Balance: "
                f"{self.example_bank_account._BankAccount__balance}"
                )
        # Act & Assert
        self.assertEqual(expected,str(self.example_bank_account))

"""