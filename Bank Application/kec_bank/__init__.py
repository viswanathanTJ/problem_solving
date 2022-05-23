from typing import Dict, Set
from kec_bank.user_handler import UserHandler


users: Dict[int, UserHandler] = dict()
acc_checker: Set[int] = set()

class Bank:
    """ KEC Bank """

    def __init__(self, account_start = 1):
        self.account_number: int = account_start
        self.ifsc = 'KEC001'

    def create_new_account(self, name: str, mobile: int):
        if mobile in acc_checker:
            print("Unable to add. User already exists in this bank.")
            return
        cur_acc_no = self.account_number
        acc_checker.add(mobile)
        users[cur_acc_no] = UserHandler(name, cur_acc_no, mobile, self.ifsc)
        print("Account created successfully")
        self.account_number += 1

    def deposit(self, acc_no: int, amt: int):
        if acc_no not in users:
            print("Failed to deposit in account", acc_no)
            return
        if amt > 1000:
            print('Unable to deposit more than 1000')
        else:
            cur_user = users[acc_no]
            if cur_user.deposit(amt):
                print('Deposit successful.')
            else:
                print('Deposit Failed.')

    