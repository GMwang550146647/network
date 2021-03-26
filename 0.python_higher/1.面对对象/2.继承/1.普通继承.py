class Contact():
    _all_contact=[]
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self._all_contact.append(self)
        print('Contact._all_contact:{}'.format(Contact._all_contact))

class Supplier(Contact):
    '''
     1.__init__默认会这样调用！不写就用父类的，写了就覆盖父类的
    '''
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)

    def order(self,order):
        print("Sent {} order to {}".format(order,self.name))


if __name__ == '__main__':
    c=Contact("Some body","somebody@example.com")
    s=Supplier("Some body","somebody@example.com")
    print(Contact._all_contact)