from typing import Dict, Set
from kec_bank.user_handler import UserHandler

### GLOBAL VARIABLES
users: Dict[int, UserHandler] = dict() # Account Number : UserHandler
acc_checker: Set[int] = set() # Contains Mobile number

#

class Bank:
    """ KEC Bank """

    def __init__(self, account_start = 1):
        self.account_number: int = account_start
        self.ifsc = 'KEC001'

    def create_new_account(self, name: str, mobile: int):
        if mobile in acc_checker:
            print("Unable to add. User already exists in this bank.")
            return
        if len(str(mobile)) < 5:
            print("Mobile number should be atleast 5 digits")
            return
        cur_acc_no = self.account_number
        acc_checker.add(mobile)
        users[cur_acc_no] = UserHandler(name, cur_acc_no, mobile, self.ifsc)
        print("Account created successfully")
        print("[*] Your account number is", cur_acc_no)
        self.account_number += 1

    def get_user(self, acc_no: int) -> UserHandler:
        """ Return current user object """
        if acc_no in users:
            return users[acc_no]
        else:
            return None

    def deposit(self, acc_no: int, amt: int):
        cur_user = self.get_user(acc_no)
        if cur_user is None:
            print("Failed to deposit in account", acc_no)
            return
        if amt > 1000:
            print('Unable to deposit more than 1000')
        else:
            cur_user.deposit(amt)
            print('Deposit successful.')

    def withdraw(self, acc_no: int, amt: int):
        cur_user = self.get_user(acc_no)
        if cur_user is None:
            print("Failed to withdraw from account", acc_no)
            return
        if cur_user.withdraw(amt):
            print("Withdrawl successful.")
        else:
            print("Withdrawl failed minimum balance 100 required.")
    
    def balance(self, acc_no: int):
        cur_user = self.get_user(acc_no)
        if cur_user is None:
            print("Failed to get balance from account", acc_no)
            return
        print("Current Balance is: {}".format(cur_user.get_balance()))
    
    def all_account_holder(self):
        print("*"*20)
        for user in users.values():
            print(user)
        print("*"*20)

    def close_account(self, acc_no: int):
        if acc_no in users:
            acc_checker.remove(users[acc_no].get_mobile_no())
            del users[acc_no]
            print("User account closed successfully")
        else:
            print("Failed to close", acc_no)

    def modify_account(self, acc_no: int, name: str):
        cur_user = self.get_user(acc_no)
        if cur_user is None:
            print("Failed to modify on account", acc_no)
            return
        cur_user.modify(name)
        print("Name modified successfully")
