class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesn't have {} but only {} left".format(amount,balance))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance


if __name__ == '__main__':

    try:
        raise InvalidWithdrawal(25, 50)
    except InvalidWithdrawal as err:
        print(err)
