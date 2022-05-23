from kec_bank.models.user import User

class UserHandler(User):
    
    def __init__(self, *args, **kwargs):
        super(UserHandler, self).__init__(*args, **kwargs)

    def deposit(self, amt: int) -> None:
        self.balance += amt

    def withdrawl(self, amt: int) -> bool:
        new_balance = self.balance - amt
        if new_balance >= 100:
            self.balance = new_balance
            return True
        return False