"""
Description: Unit tests for the BankAccount class.
Author: Rowan Mullin
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from datetime import date
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):
    
	def setUp(self):
		self.example_data = [100,100,100.00,date(2025,10,1),100.00]
		self.example_investment_account = InvestmentAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],self.example_data[3],
			self.example_data[4])

	def test_init_valid(self):
		self.assertEqual(self.example_data[0],
			self.example_investment_account._BankAccount__account_number)
		self.assertEqual(self.example_data[1],
			self.example_investment_account._BankAccount__client_number)
		self.assertEqual(self.example_data[2],
			self.example_investment_account._BankAccount__balance)
		self.assertEqual(self.example_data[3],
			self.example_investment_account._date_created)
		self.assertEqual(self.example_data[4],
			self.example_investment_account._InvestmentAccount__management_fee)
		
	def test_init_invalid_management_fee(self):
		invalid_investment_account = InvestmentAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],self.example_data[3],
			"")
		self.assertEqual(2.55,
			invalid_investment_account._InvestmentAccount__management_fee)
	
	def test_get_service_charges_date_above_10years(self):
		invalid_investment_account = InvestmentAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],date(2000,10,1),
			self.example_data[4])
		self.assertEqual(0.5,
			invalid_investment_account.get_service_charges())
	
	def test_get_service_charges_date_below_10years(self):
		invalid_investment_account = InvestmentAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],date(2023,10,1),
			self.example_data[4])
		self.assertEqual(100.5,
			invalid_investment_account.get_service_charges())
	
	def test_get_service_charges_date_equals_10years(self):
		invalid_investment_account = InvestmentAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],
			date(date.today().year + 10,date.today().month,date.today().day),
			self.example_data[4])
		self.assertEqual(100.5,
			invalid_investment_account.get_service_charges())
		
	def test_str_date_more_than_10_years(self):
		example_account = InvestmentAccount(self.example_data[0],
			self.example_data[1],self.example_data[2],
			date(2000,10,1),
			self.example_data[4])
		self.assertEqual(
			("Account Number: 100 Balance: $100.00"+
			f"\nDate Created: 2000-10-01 Management Fee: "+
			f"Waived Account Type: Investment\n"), 
			str(example_account))
		
	def test_str_date_within_10_years(self):
		self.assertEqual(
			("Account Number: 100 Balance: $100.00"+
			f"\nDate Created: 2025-10-01 Management Fee: "+
			f"$100.00 Account Type: Investment\n"), 
			str(self.example_investment_account))
