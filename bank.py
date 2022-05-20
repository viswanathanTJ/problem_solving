users = []
acc_no = 101
user_locator = {}

def add_user(name):
    global acc_no, users, user_locator
    d = {}
    d['name'] = name
    d['accno'] = acc_no
    user_locator[acc_no] = len(users)
    acc_no += 1
    d['ifsc'] = 'IFSC01'
    d['amt'] = 500
    users.append(d)
    print('added successfully')
    print(d)


def get_user(acc_no):
    global users, user_locator
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
        # print(user)

bank_open = True

while bank_open:
    print('''
    1. Add user
    2. Get user
    3. Deposit
    4. Withdrawl
    5. Display all users
    0. Exit
''')
    choice = int(input())
    match choice:
        case 1:
            name = input('Enter user name: ')
            add_user(name)
        case 2:
            accno = int(input('Enter account number: '))
            user = get_user(accno)
            if user is not None:
                print(user)
            else:
                print('User not found')
        case 3:
            accno = int(input('Enter account number: '))
            amt = int(input('Enter amount to deposit: '))
            deposit(accno, amt)
        case 4:
            accno = int(input('Enter account number: '))
            amt = int(input('Enter amount to withdrawl: '))
            withdraw(accno, amt)
        case 5:
            display_all_user()
        case 0:
            bank_open = False

print('Good Bye...')
