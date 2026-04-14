"""
Description: Unit tests for the BankAccount class.
Author: Rowan Mullin
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):
    
	def setUp(self):
		self.example_data = [100,100,100.00,date(2025,10,1),100.00,0.01]
		self.example_chequing_account = ChequingAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],self.example_data[3],
			self.example_data[4],self.example_data[5])

	def test_init_valid(self):
		self.assertEqual(self.example_data[0],
			self.example_chequing_account._BankAccount__account_number)
		self.assertEqual(self.example_data[1],
			self.example_chequing_account._BankAccount__client_number)
		self.assertEqual(self.example_data[2],
			self.example_chequing_account._BankAccount__balance)
		self.assertEqual(self.example_data[3],
			self.example_chequing_account._date_created)
		self.assertEqual(self.example_data[4],
			self.example_chequing_account._ChequingAccount__overdraft_limit)
		self.assertEqual(self.example_data[5],
			self.example_chequing_account._ChequingAccount__overdraft_rate)
		
	def test_init_invalid_overdraft_limit(self):
		invalid_chequing_account = ChequingAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],self.example_data[3],
			"",self.example_data[5])
		self.assertEqual(-100,
			invalid_chequing_account._ChequingAccount__overdraft_limit)
	
	def test_init_invalid_overdraft_rate(self):
		invalid_chequing_account = ChequingAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],self.example_data[3],
			self.example_data[4],"")
		self.assertEqual(0.05,
			invalid_chequing_account._ChequingAccount__overdraft_rate)

	def test_init_invalid_date(self):
		invalid_chequing_account = ChequingAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],"",self.example_data[4],
			self.example_data[5])
		self.assertEqual(date.today(),
			invalid_chequing_account._date_created)
	
	def test_get_service_charges_balance_above_limit(self):
		invalid_chequing_account = ChequingAccount(self.example_data[0],
			self.example_data[1],11,self.example_data[3],10,
			self.example_data[5])
		self.assertEqual(0.5,
			invalid_chequing_account.get_service_charges())
	
	def test_get_service_charges_balance_below_limit(self):
		invalid_chequing_account = ChequingAccount(self.example_data[0],
			self.example_data[1],9,self.example_data[3],10,
			self.example_data[5])
		self.assertEqual(0.51,
			invalid_chequing_account.get_service_charges())
	
	def test_get_service_charges_balance_equal_limit(self):
		invalid_chequing_account = ChequingAccount(self.example_data[0],
			self.example_data[1],10,self.example_data[3],10,
			self.example_data[5])
		self.assertEqual(0.5,
			invalid_chequing_account.get_service_charges())
		
	def test_str_valid(self):
		self.assertEqual("Account Number: 100 Balance: $100.00"+
		"\nOverdraft Limit: $100.00 Overdraft Rate: 1.00% Account Type: "+
		"Chequing\n",
			str(self.example_chequing_account))
