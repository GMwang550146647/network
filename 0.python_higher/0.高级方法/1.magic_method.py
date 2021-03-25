aaaa=1000
class GSD():  # 在python3中GSD是新式类,它实现了三种方法,这个类就被称作一个描述符
    '''
    descriptor的实例自己访问自己是不会触发__get__，而会触发__call__，只有descriptor作为其它类的属性才有意义
    '''

    def __get__(self, instance, owner):
        '''
        __get__():调用一个属性时,触发
        '''
        print('__get__调用...: __dict__', self.__dict__, instance, owner)
        return self.__dict__['x']

    def __set__(self, instance, value):
        '''
        __set__():为一个属性赋值时,触发
        '''
        print('__set__设置...: __dict__', self.__dict__, instance, value)
        self.__dict__['x'] = value

    def __delete__(self, instance):
        '''
        __delete__():采用del删除属性时,触发
        '''
        print('__delete__删除...', instance)


class Demo2(object):
    gsd = GSD()

    def __init__(self):
        global aaaa
        self.gsd = 10


class Demo(object):
    gggg = 'To be happy...'
    _meta = {}

    def __init__(self, gsd):
        self.name = 'gmwang'
        self.record = {}
        self.lt = [1, 2, 3, 4, 5, 6, 7]
        self.dt = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    def some_method(self):
        return 'You are handsome!'

    def __repr__(self):
        '''
        没有__str__()的时候这个顶上
        '''
        return 'This is a gmwang_str !'

    def __str__(self):
        '''
        调用print/或者作为字符串的时候调用
        '''
        return 'lovely feifei~'

    def __bytes__(self):
        '''
        调用bytes()的时候调用
        :return:
        '''
        return b'abcde'

    def __hash__(self):
        '''
        调用hash()的时候调用
        :return:
        '''
        return 1000001111

    def __setattr__(self, key, value):
        '''
        注意 该函数 在设置  self.xxx=xxx的时候其实是调用该函数 (默认写入 __dict__中)
        '''
        print("****************__setattr__******************")
        print('origin__dict__:{}'.format(self.__dict__))
        print('origin_meta:{}'.format(self._meta))
        self._meta[key] = value
        # self.__dict__[key] = value
        print('modified__dict__:{}'.format(self.__dict__))
        print('modified_meta:{}'.format(self._meta))

    def __getattr__(self, key):
        '''
        在__getattribute__中找不到改属性的时候会在__getattr__中解决
        因为__getattribute__都是在 __dict__中查找属性值的
        print obj.name
        print obj.__dict__['name']
        print getattr(obj, 'name')
        '''
        print("****************__getattr__******************")
        try:
            print('self._meta[key] ->', self._meta[key])
            return self._meta[key]
        except:
            raise AttributeError

    # def __getattribute__(self, key):
    #     """
    #     getattr 的时候会调用，其实都是往__dict__里面去拿函数或者变量！
    #         这个不要随便重写！很容易玩完...递归栈溢出
    #
    #     """
    #     try:
    #         return super(Demo).__getattribute__(key)
    #     except:
    #         if key in self._meta:
    #             return self._meta[key]
    #         else:
    #             raise AttributeError

    def __delattr__(self, item):
        '''
        删除属性 del self.xxx 的时候使用
            本来默认是删除 __dict__中的对应值的，现在不行了！因为改写了
        '''
        if item in self._meta:
            print("Before del {}: {}".format(item, self._meta))
            print("Before del {}: {}".format(item, self.__dict__))
            del self._meta[item]
            print("After del {}: {}".format(item, self._meta))
            print("After del {}: {}".format(item, self.__dict__))
        else:
            print("Attribute {} not found!".format(item))

    def __dir__(self):
        """
        使用 dir()的时候调用
            默认返回该类拥有的所有 函数和变量 （包括magic methods)
        """
        # 由于返回之后他还会排序一下，所以好好看看结果！对你很重要！
        return "🐷 是 其 猪 你 实 猪".split()

    def __call__(self, *args, **kwargs):
        '''
        调用 实例对象() 的使用运行
        '''
        self.main()

    def __setitem__(self, key, value):
        '''
        obj['key']=value
        '''
        self.dt[key] = value

    def __getitem__(self, item):
        '''
        obj['key']
        '''
        return self.dt.get(item, None)

    def __iter__(self):
        '''
        for xxx in obj:
            ...
        '''
        self.a = 0
        return self

    def __next__(self):
        '''
        用于 next() 函数
        '''
        if self.a < 2:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

    def __reversed__(self):
        '''
        reversed的时候输出
        '''
        return '逆转之后的list:{}'.format(str(list(reversed(list(self.dt.keys())))))

    def __contains__(self, item):
        '''
        xxx in obj
        '''
        return item in self.dt

    def __enter__(self):
        '''
        用于with的开始
        '''
        print("Enter!   Before Doing Something")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        用于with的结束
        """
        print("Exit!   After Doing Something")

    def main(self):
        print(self.__dict__)
        print(self.__class__)


if __name__ == '__main__':
    a = Demo(10)
    print(a)
    print(a.name)
    del a.name
    print(a._meta)
    print(bytes(a))
    print(hash(a))
    print(dir(a))
    print(getattr(a, 'some_method')())
    a.name = 'feifei猪'

    b = Demo2()
    print(b.gsd)
    del b.gsd

    a()
    print(reversed(a))
    print(a['a'])
    a['b'] = 100
    print('c' in a)
    print(reversed(a))
    for item in a:
        print(item)

    with a:
        print("Doing Something!")
