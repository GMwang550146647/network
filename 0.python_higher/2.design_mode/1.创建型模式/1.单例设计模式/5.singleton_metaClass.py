class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("****Here is myInt!")
        print("Do whatever you want with these objects")
        print("MyInt __call__  args:{},kwargs:{}".format(args, kwargs))
        return super().__call__(*args, **kwargs)  # 这里的参数会传进去 子类的initial!


class int(metaclass=MyInt):
    def __init__(self, x, y):
        print('int __init__', x, y)
        self.x = x
        self.y = y

    def __new__(cls, *args, **kwargs):
        print('int __new__ args:{},kwargs:{}'.format(args, kwargs))
        return super().__new__(cls)


class MetaSingleton(type):
    _instance = {}
    '''
    此类的__call__将影响子类的初始化
    '''

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
            for kwarg_i in kwargs:
                cls._instance[cls].__dict__[kwarg_i] = kwargs[kwarg_i]
            print("MetaSingleton _instance:{}".format(cls._instance))
            return cls._instance[cls]
        else:
            return cls._instance[cls]


class Logger1(metaclass=MetaSingleton):
    def __init__(self, *args, **kwargs):
        pass

    def func_safe(self):
        '''
        这里的操作保证单线程安全！
        '''
        print('Hello world!')


class Logger2(metaclass=MetaSingleton):
    def __init__(self, *args, **kwargs):
        pass

    def func_safe(self):
        '''
        这里的操作保证单线程安全！
        '''
        print('Hello world!')


if __name__ == '__main__':
    '''
    1.test for metaclass
    '''
    i = int(4, 5)
    print(i.x)

    '''
    2.test for Singleton MetaClass
    '''
    lg1 = Logger1(a=1, b=2, c=3)
    lg2 = Logger1(d=4)
    print('lg1.a', lg1.a)
    print(lg1.__dict__)
    print(lg1 is lg2)

    '''
    3.test for multi Singleton
    '''
    lg2 = Logger2()
