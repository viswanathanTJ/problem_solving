users = []
acc_no = 101
user_locator = {}

def new_account(name):
    global acc_no, users, user_locator
    d = {}
    d['name'] = name
    d['accno'] = acc_no
    user_locator[acc_no] = len(users)
    acc_no += 1
    d['ifsc'] = 'IFSC01'
    d['amt'] = 500
    users.append(d)
    print('Account created successfully')
    print(d)


def get_user(acc_no):
    global users, user_locator
    print(user_locator)
    print(users)
    if acc_no in user_locator:
        return users[user_locator[acc_no]]
    return None


def get_balance(accno):
    cur_user = get_user(accno)
    if cur_user is not None:
        return cur_user['amt']
    else:
        return None

def withdraw(accno, amt):
    cur_user = get_user(accno)
    if cur_user['amt'] - 100 >= amt:
        cur_user['amt'] -= amt
        print('Withdrawl of amt', amt, 'is successful')
        print('Current balance is', get_balance(accno))
    else:
        print('Withdrawl unsuccessfull. Minimum balance 100 required!!!')


def deposit(accno, amt):
    cur_user = get_user(accno)
    if amt >= 1000:
        print('Deposit below 1000 only availble')
    else:
        cur_user['amt'] += amt
        print('Deposit successful.')
        print('Current balance is', get_balance(accno))

def display_all_user():
    global users
    for user in users:
        [print(key, ':', value) for key, value in user.items()]
        print()

def close_account(acc_no):
    cur_acc = get_user(acc_no)
    print(cur_acc)
    if cur_acc is not None:
        del cur_acc
        print('Successfuly closed', acc_no)
    else:
        print('Account does not exists')

def modify_account(acc_no):
    if get_user(acc_no):
        new_name = input('Enter new name: ')
        users[acc_no].name = new_name
        print('Successfully modified')
    else:
        print('Account not exists')

bank_open = True

while bank_open:
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
            name = input('Enter user name: ')
            new_account(name)
        case 2:
            accno = int(input('Enter account number: '))
            amt = int(input('Enter amount to deposit: '))
            deposit(accno, amt)
        case 3:
            accno = int(input('Enter account number: '))
            amt = int(input('Enter amount to withdrawl: '))
            withdraw(accno, amt)
        case 4:
            accno = int(input('Enter account number to get balance: '))
            print(get_balance(accno))
        case 5:
            display_all_user()
        case 6:
            accno = int(input('Enter account number to close: '))
            close_account(acc_no)
        case 7:
            accno = int(input('Enter account number to modify: '))
            modify_account(acc_no)
        case 0:
            bank_open = False

print('Good Bye...')
