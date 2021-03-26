"""
suggestion:
    如果你认为你需要多重继承，那么你有可能是错误的，如果你知道你需要他，你可能是正确的
"""

class Contact():
    _all_contact = []

    def __init__(self, name, email):
        self.c_name = name
        self.email = email
        self._all_contact.append(self)
        print('Contact._all_contact:{}'.format(Contact._all_contact))

    def send_mail(self, message):
        print("Class Contact: Sending mail '{}' to {}".format(message, self.email))


class MailSender:
    _all_contact = []

    def __init__(self, name, email):
        self.m_name = name
        self.email = email
        self._all_contact.append(self)
        print('MailSender._all_contact:{}'.format(Contact._all_contact))

    def send_mail(self, message):
        print("Class MailSender: Sending mail '{}' to {}".format(message, self.email))


class EmailableContact(Contact, MailSender):
    def __init__(self, *args, **kwargs):
        """
        默认的初始化函数是最右边的（因为会覆盖）
        但是可以自己改写
        """
        MailSender.__init__(self, *args, **kwargs)
        Contact.__init__(self, *args, **kwargs)

        print("EmailableContact: __dict__:{}".format(self.__dict__))



if __name__ == '__main__':
    e = EmailableContact("Aaron", 'aaron@qpple.com')

    e.send_mail('Hello From EmailableContact')
