from abc import ABCMeta, abstractmethod

'''

'''


class You:
    def __init__(self):
        print("You :: Let's buy the Denim shirt! ")
        self.debitCard = DebitCard()
        self.isPurcharsed = None

    def make_payment(self):
        self.isPurcharsed = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurcharsed:
            print("You:: Wow! Denim shirt is Mine :-)")
        else:
            print("You:: I should earn more :(")


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


'''
1.本体：功能最齐全，但是直接对其修改会存在许多非法的操作
'''


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card
        return self.account

    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(), " has enough funds")
        return True

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False


'''
2.代理：只有Bank的部分功能！ 其提供给自己的特定合法功能！继承自同一个类！
'''


class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()


if __name__ == '__main__':
    You().make_payment()
