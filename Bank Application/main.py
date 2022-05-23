from kec_bank import Bank

def start_bank():
    bank = Bank()
    bank_open = True
    while bank_open:
        try:
            print('''
1. NEW ACCOUNT
2. DEPOSIT AMOUNT
3. WITHDRAW AMOUNT
4. BALANCE ENQUIRY
5. ALL ACCOUNT HOLDER LIST
6. CLOSE AN ACCOUNT
7. MODIFY AN ACCOUNT
8. EXIT
''')
            choice = int(input())
            match choice:
                case 1:
                    name = input("Enter User Name: ")
                    mobile = int(input("Enter Mobile Number: "))
                    bank.create_new_account(name, mobile)
                case 2:
                    acc_no = int(input("Enter account number: "))
                    amt = int(input("Enter amount to deposit: "))
                    bank.deposit(acc_no, amt)
                case 3:
                    acc_no = int(input("Enter account number: "))
                    amt = int(input("Enter amount to withdraw: "))
                    bank.withdraw(acc_no, amt)
                case 4:
                    acc_no = int(input("Enter account number to get balance: "))
                    bank.balance(acc_no)
                case 5:
                    bank.all_account_holder()
                case 6:
                    acc_no = int(input("Enter account number to close: "))
                    bank.close_account(acc_no)
                case 7:
                    acc_no = int(input("Enter account number to modify: "))
                    new_name = input("Enter new name for account: ")
                    bank.modify_account(acc_no, new_name)
                case 8:
                    bank_open = False
        except KeyboardInterrupt:
            break
        except Exception as err:
            print("Error:", err)
    print("Thank you for visiting.\nGood Bye..\nVisit Again :)")

if __name__ == '__main__':
    start_bank()