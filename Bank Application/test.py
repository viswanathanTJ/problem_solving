from kec_bank import Bank

bank = Bank()

bank.create_new_account('viswa', 123)
bank.create_new_account('siva', 1234)

bank.deposit(1, 1000)
bank.withdraw(1, 500)

bank.balance(1)

bank.all_account_holder()

bank.close_account(1)

bank.all_account_holder()

bank.modify_account(2, 'viswa')

bank.all_account_holder()
