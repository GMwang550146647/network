'''
1.拓展list
'''


class ContactList(list):
    def search(self, name):
        matching_contact = []
        for contact in self:
            if name in contact.name:
                matching_contact.append(contact)
        return matching_contact


'''
2.拓展dict
'''


class LongNameDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._longest_key = None

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if not self._longest_key or len(self._longest_key) < len(key):
            self._longest_key = key


class Contact():
    _all_contact = ContactList()
    _contact2email = LongNameDict()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self._all_contact.append(self)
        self._contact2email[name]=email
        print('Contact._all_contact:{}'.format(Contact._all_contact))
        print("Contact._contact2email:{}  , max_key:{}".format(Contact._contact2email,Contact._contact2email._longest_key))


class Supplier(Contact):

    def order(self, order):
        print("Sent {} order to {}".format(order, self.name))


if __name__ == '__main__':
    c = Contact("Some body", "somebody@example.com")
    s = Supplier("Some body1dfasdfafafd", "somebody@example.com")
    s2 = Supplier("Some body2", "somebody@example.com")
    s3 = Supplier("Someone2", "somebody@example.com")
    targets = [c.name for c in Contact._all_contact.search('body')]
    print(targets)
