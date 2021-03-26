"""
suggestion:
    如果你认为你需要多重继承，那么你有可能是错误的，如果你知道你需要他，你可能是正确的

注意！
    super() 调用的不绝对是父类的对象！ 其实是上一个对象 例如这里的MailSender1 调用的是MailSender2的 对象！
"""


class MailSender_base():
    _all_contact = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

        self._all_contact.append(self)
        print('MailSender_base._all_contact:{}'.format(MailSender_base._all_contact))

    def send_mail(self, message):
        print("Class MailSender_base: Sending mail '{}' to {}".format(message, self.email))


class MailSender1(MailSender_base):
    _all_contact = []

    def __init__(self, name, email):
        super().__init__(name, email)
        self.c_name = name
        self.email = email
        self._all_contact.append(self)
        print('MailSender1._all_contact:{}'.format(MailSender1._all_contact))

    def send_mail(self, message):
        super().send_mail(message)
        print("Class MailSender1: Sending mail '{}' to {}".format(message, self.email))


class MailSender2(MailSender_base):
    _all_contact = []

    def __init__(self, name, email):
        super().__init__(name, email)
        self.m_name = name
        self.email = email
        self._all_contact.append(self)

        print('MailSender2._all_contact:{}'.format(MailSender2._all_contact))

    def send_mail(self, message):
        super().send_mail(message)
        print("Class MailSender2: Sending mail '{}' to {}".format(message, self.email))


class MailSenderCombine(MailSender1, MailSender2):
    _all_contact = []

    def __init__(self, name, email):
        """
        默认的初始化函数是最右边的（因为会覆盖）
        但是可以自己改写
        """
        super().__init__(name, email)
        self.m_name = name
        self.email = email
        self._all_contact.append(self)
        print('MailSenderCombine._all_contact:{}'.format(MailSender2._all_contact))

    def send_mail(self, message):
        super().send_mail(message)
        print("EmailableContact: Sending mail '{}' to {}".format(message, self.email))


if __name__ == '__main__':
    e = MailSenderCombine("Aaron", 'aaron@qpple.com')

    e.send_mail('Hello From EmailableContact')
