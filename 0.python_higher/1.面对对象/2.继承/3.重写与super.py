class Contact():
    _all_contact = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self._all_contact.append(self)
        print('Contact._all_contact:{}'.format(Contact._all_contact))


class Friend(Contact):
    '''
     1.__init__默认会这样调用！不写就用父类的，写了就覆盖父类的
    '''

    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone




if __name__ == '__main__':
    c = Contact("Some body", "somebody@example.com")
    s = Friend("gmwang", "gmwang@example.com",18312030444)
    print(Contact._all_contact)
