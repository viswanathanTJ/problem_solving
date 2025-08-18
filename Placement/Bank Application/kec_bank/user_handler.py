from kec_bank.models.user import User


class UserHandler(User):
    
    def __init__(self, *args, **kwargs):
        super(UserHandler, self).__init__(*args, **kwargs)

    def deposit(self, amt: int) -> None:
        self._balance += amt

    def withdraw(self, amt: int) -> bool:
        new_balance = self._balance - amt
        if new_balance >= 100:
            self._balance = new_balance
            return True
        return False

    def modify(self, name: str) -> None:
        self._name = name

    def get_balance(self) -> int:
        return self._balance

    def get_mobile_no(self) -> int:
        return self._mobile 

    def get_acc_no(self) -> int:
        return self._acc_no

    def get_user_name(self) -> str:
        return self._name

    def get_ifsc(self) -> str:
        return self._ifsc
