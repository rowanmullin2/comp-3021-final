__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Rowan Mullin"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    
    def __init__(self):
        """
        Initializes the Client Lookup window by loading the client and 
        account data and setting up the button connections.

        Loads the client and account data using the load_data() function 
        from manage_data.py. Connects the lookup button, 
        client_number_edit and account_table to their respective slots.
        """
        super().__init__()

        self.__client_listing, self.__accounts = load_data()

        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(
            self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        self.filter_button.clicked.connect(self.__on_filter)

    @Slot()
    def __on_lookup_client(self) -> None:
        """
        Called when the lookup button is clicked.

        Retrieves the client number from the client_number_edit field 
        and attempts to retrieve the corresponding Client object from 
        the __client_listing dictionary. If the client number is not a 
        numeric value, a warning message box is displayed with an error 
        message and the display is reset.

        If the client is not found, a warning message box is displayed 
        with a not found message and the display is reset.

        If the client is found, the client information is displayed in 
        the client_info_label and the associated accounts are retrieved 
        from the __accounts dictionary and displayed in the 
        account_table. The table is resized to fit the contents of the 
        table.

        returns: None
        """
        client_num = self.client_number_edit.text()
        client = self.__client_listing.get(client_num)

        try: 
            client_num = int(client_num)
        except ValueError:
            QMessageBox.warning(
                self, "Input Error", 
                "The client number must be a numeric value.")
            self.reset_display()
            return

        if client is None:
            QMessageBox.warning(
                self, "Not Found", 
                f"Client number: {client_num} not found.")
            self.reset_display()
            return
        
        self.client_info_label.setText(client.first_name + " " 
            + client.last_name)
        
        self.__toggle_filter(False)

        for account in self.__accounts.values():
            if account.client_number == client.client_number:
                rowCount = self.account_table.rowCount()
                self.account_table.insertRow(rowCount)

                account_number_item = QTableWidgetItem(
                    str(account.account_number))
                account_balance_item = QTableWidgetItem(
                    f"${account.balance:,.2f}")
                account_date_created_item = QTableWidgetItem(
                    str(account._date_created))
                account_type_item = QTableWidgetItem(type(account).__name__)

                self.account_table.setItem(rowCount, 0, account_number_item)
                self.account_table.setItem(rowCount, 1, account_balance_item)
                self.account_table.setItem(rowCount, 2, 
                    account_date_created_item)
                self.account_table.setItem(rowCount, 3, account_type_item)

                self.account_table.resizeColumnsToContents()

    @Slot()
    def __on_text_changed(self) -> None:
        """
        Called when the text in the client number edit field changes.

        Clears the account table by setting its row count to 0.
        """
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self,row: int, column: int) -> None:
        """
        Called when an item in the account table is selected.

        Displays a warning message box if the selected item is not a 
        valid bank account and resets the display.

        If the selected item is a valid bank account, creates a new
        AccountDetailsWindow with the selected bank account and connects
        its balance_updated signal to the update_data slot. Finally, 
        shows the AccountDetailsWindow using the exec() method.

        Args:
            row (int): The row of the selected item in the account table.
            column (int): The column of the selected item in the account 
            table.
        """
        account_number = int(self.account_table.item(row, 0).text())

        if account_number is None:
            QMessageBox.warning(
                self, "Invalid Selection", 
                f"Please select a valid record.")
            self.reset_display()
            return
        
        account = self.__accounts.get(account_number)
        if account is None:
            QMessageBox.warning(
                self, "No Bank Account", 
                f"Bank Account selected does not exist.")
            return

        account_details_window = AccountDetailsWindow(account)
        account_details_window.balance_updated.connect(self.__update_data)
        account_details_window.exec_()

    def __update_data(self, account: BankAccount) -> None:
        """
        Updates the display with the updated BankAccount object.

        Iterates through the rows of the account table and checks if the
        account number in the row matches the account number of the 
        given BankAccount object. If a match is found, the balance item 
        in the row is updated with the new balance from the BankAccount 
        object.

        The updated BankAccount object is also stored in the __accounts
        dictionary for later use.

        Finally, the update_data function is called recursively with the
        updated BankAccount object to ensure that all accounts in the
        display are updated.
        """
        for row in range(self.account_table.rowCount()):
            if int(self.account_table.item(row, 0).text()
                   ) == account.account_number:
                account_balance_item = QTableWidgetItem(
                    f"${account.balance:,.2f}")
                self.account_table.setItem(row, 1, account_balance_item)
                self.__accounts[account.account_number] = account
                update_data(account)
                break        

    @Slot()
    def __on_filter(self) -> None:
        """
        Called when the filter button is clicked.

        Applies a filter to the account table based on the filter type 
        and key entered in the filter edit field. If the filter button 
        text is "Apply Filter", the filter is applied by hiding rows 
        that do not contain the filter key in the column specified by 
        the filter type. If the filter button text is "Clear Filter", 
        all rows are unhidden and the filter edit field is cleared.

        Args:
            None

        Returns:
            None
        """
        if self.filter_button.text() == "Apply Filter":
            filter_type = self.filter_combo_box.currentIndex()
            filter_key = self.filter_edit.text().lower().strip()

            for row in range(self.account_table.rowCount()):
                if filter_key not in self.account_table.item(row, filter_type
                    ).text().lower():
                    self.account_table.setRowHidden(row, True)
                    
            self.__toggle_filter(True)
        else:
            self.__toggle_filter(False)

    def __toggle_filter(self, filter_on: bool) -> None:
        """
        Toggles the filter on or off based on the given parameter.

        Args:
            filter_on (bool): If True, the filter is applied and the 
            filter button text is set to "Reset". If False, the filter 
            is cleared and the filter button text is set to 
            "Apply Filter".

        Returns:
            None
        """
        self.filter_button.setEnabled(True)

        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.filter_label.setText("Data is Not Currently Filtered")

