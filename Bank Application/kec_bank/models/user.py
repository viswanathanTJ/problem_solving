class User:
    """ User Details """

    def __init__(self, name: str, acc_no: int, mobile: int, ifsc: str):
        self._name = name
        self._acc_no = acc_no
        self._balance = 100
        self._mobile = mobile
        self._ifsc = ifsc

    def __str__(self):
        return "Name: {}\nAccount Number: {}\nBalance: {}\nIFSC Code: {}"\
            .format(self._name, self._acc_no, self._balance, self._ifsc)
