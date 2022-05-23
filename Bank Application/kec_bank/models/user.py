class User:
    """ User Details """
    def __init__(self, name: str, acc_no: int, mobile: int, ifsc: str):
        self.name = name
        self.acc_no = acc_no
        self.balance = 100
        self.ifsc = ifsc

    def __str__(self):
        return "Name: {}\nAccount Number: {}\nBalance: {}\nIFSC Code: {}"\
            .format(self.name, self.acc_no, self.balance, self.ifsc)