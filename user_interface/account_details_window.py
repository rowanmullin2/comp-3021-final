__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Rowan Mullin"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account 
    transactions.
    """

    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        
        """
        Initializes the Account Details window with a given BankAccount 
        object.

        Args:
            account (BankAccount): A BankAccount object containing the 
            account details.

        If the account object is not a BankAccount, the window will be 
        rejected.

        Sets the account number and balance labels to the corresponding 
        values from the given BankAccount object.
        
        Connects the deposit, withdraw and exit buttons to their 
        respective slots.
        """
        super().__init__()

        #not bank account
        if account is not BankAccount:
            self.reject()

        self.__account = copy.deepcopy(account)
        
        self.account_number_label.setText(str(self.__account.account_number))
        self.balance_label.setText(f"${self.__account.balance:,.2f}")

        self.deposit_button.clicked.connect(self.__on_apply_transaction)
        self.withdraw_button.clicked.connect(self.__on_apply_transaction)
        self.exit_button.clicked.connect(self.__on_exit)

    @Slot()
    def __on_apply_transaction(self) -> None:
        """
        Called when the Deposit or withdraw buttons are clicked. 

        Validates the transaction amount input and performs the relevant 
        transaction (deposit or withdraw) on the BankAccount object. If 
        the transaction is successful, updates the balance label and 
        resets the transaction amount edit field. If the transaction 
        fails, a warning message box is displayed with the error 
        message. Finally, emits the balance_updated signal with the 
        updated BankAccount object.
        """
        try:
            transaction_amount = float(self.transaction_amount_edit.text())
        except:
            QMessageBox.warning(
                self, "Invalid Data", 
                "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return
        
        try:
            if(self.sender() == self.deposit_button):
                transactionType = "Deposit"
                self.__account.deposit(transaction_amount)
            elif(self.sender() == self.withdraw_button):
                transactionType = "Withdraw"
                self.__account.withdraw(transaction_amount)

            self.balance_label.setText(f"${self.__account.balance:,.2f}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()
            
        except Exception as e:
            QMessageBox.warning(
                self, f"{transactionType} Failed", 
                str(e))
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()
            return
        
        self.balance_updated.emit(self.__account)

    @Slot()
    def __on_exit(self) -> None:
        """
        Called when the exit button is clicked.

        Closes the window.
        """
        self.close()
