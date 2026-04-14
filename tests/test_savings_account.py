"""
Description: Unit tests for the BankAccount class.
Author: Rowan Mullin
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    
	def setUp(self):
		self.example_data = [100,100,100.00,date(2025,10,1),1.00]
		self.account = SavingsAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],self.example_data[3],
			self.example_data[4])

	def test_init_valid(self):
		self.assertEqual(self.example_data[0],
			self.account._BankAccount__account_number)
		self.assertEqual(self.example_data[1],
			self.account._BankAccount__client_number)
		self.assertEqual(self.example_data[2],
			self.account._BankAccount__balance)
		self.assertEqual(self.example_data[3],
			self.account._date_created)
		self.assertEqual(self.example_data[4],
			self.account._SavingsAccount__minimum_balance)
		
	def test_init_invalid_minimum_balance(self):
		invalid_account = SavingsAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],self.example_data[3],
			"")
		self.assertEqual(50,
			invalid_account._SavingsAccount__minimum_balance)
		
	def test_get_service_charges_balance_above_minimum(self):
		self.assertEqual(0.5,
			self.account.get_service_charges())
	
	def test_get_service_charges_balance_equal_minimum(self):
		invalid_account = SavingsAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],self.example_data[3],
			100.00)
		self.assertEqual(0.5,invalid_account.get_service_charges())
	
	def test_get_service_charges_balance_below_minimum(self):
		invalid_account = SavingsAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],self.example_data[3],
			101.00)
		self.assertEqual(1.0,invalid_account.get_service_charges())
	
	def test_str_valid(self):
		self.assertEqual("Account Number: 100 Balance: $100.00"+
		"\nMinimum Balance: $1.00 Account Type: Savings\n",
		str(self.account))