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
                case 8:
                    bank_open = False
        except KeyboardInterrupt:
            break
        except Exception as err:
            print("Error:", err)

if __name__ == '__main__':
    start_bank()