class Counter(type):
    def __init__(self,*args,**kwargs):
        self.__instance=None
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance=super().__call__(*args,**kwargs)
            return self.__instance
        else:
            return self.__instance

class MyClass(metaclass=Counter):
    pass

if __name__ == '__main__':
    a=MyClass()
    b=MyClass()
    print(a==b)
    print(a is b)
    k1=a.__class__.__instance
    a.__instance=None
    k2=MyClass()
    print(k1==k2)
    print(k1 is k2)