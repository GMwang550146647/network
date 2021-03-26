"""
suggestion:
    如果你认为你需要多重继承，那么你有可能是错误的，如果你知道你需要他，你可能是正确的
"""


class MailSender_base():
    _all_contact = []

    def send_mail(self, message):
        print("Class MailSender_base: Sending mail '{}' to {}".format(message, self.email))


class MailSender1(MailSender_base):
    _all_contact = []

    def __init__(self, name, email):
        self.c_name = name
        self.email = email
        self._all_contact.append(self)
        print('MailSender1._all_contact:{}'.format(MailSender1._all_contact))

    def send_mail(self, message):
        MailSender_base.send_mail(self,message)
        print("Class MailSender1: Sending mail '{}' to {}".format(message, self.email))


class MailSender2(MailSender_base):
    _all_contact = []

    def __init__(self, name, email):
        self.m_name = name
        self.email = email
        self._all_contact.append(self)
        print('MailSender2._all_contact:{}'.format(MailSender2._all_contact))

    def send_mail(self, message):
        MailSender_base.send_mail(self, message)
        print("Class MailSender2: Sending mail '{}' to {}".format(message, self.email))


class MailSenderCombine(MailSender1, MailSender2):
    def __init__(self, *args, **kwargs):
        """
        默认的初始化函数是最右边的（因为会覆盖）
        但是可以自己改写
        """
        MailSender1.__init__(self, *args, **kwargs)
        MailSender2.__init__(self, *args, **kwargs)

        print("MailSenderCombine: __dict__:{}".format(self.__dict__))

    def send_mail(self, message):
        MailSender1.send_mail(self, message)
        MailSender2.send_mail(self, message)
        print("EmailableContact: Sending mail '{}' to {}".format(message, self.email))


if __name__ == '__main__':
    e = MailSenderCombine("Aaron", 'aaron@qpple.com')

    e.send_mail('Hello From EmailableContact')
