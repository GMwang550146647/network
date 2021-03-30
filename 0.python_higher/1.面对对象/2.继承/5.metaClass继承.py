"""
参考：
    https://zhuanlan.zhihu.com/p/98440398
从上面的运行结果可以发现在定义 class Foo() 定义时，会依次调用 MyMeta 的 __new__ 和 __init__ 方法构建 Foo 类，
然后在调用 foo = Foo() 创建类的实例对象时，才会调用 MyMeta 的 __call__ 方法来调用 Foo 类的 __new__ 和 __init__ 方法。

理解：
    1.所有的 Python 的用户定义类，都是 type 这个类的实例。
        在 Python 的类型世界里，type 这个类就是造物的上帝
    2.用户自定义类，只不过是 type 类的 __call__ 运算符重载
    3.metaclass 是 type 的子类，通过替换 type 的 __call__ 运算符重载机制，“超越变形”正常的类
        一旦你把一个类型 MyClass 的 metaclass 设置成 MyMeta，MyClass 就不再由原生的 type 创建，而是会调用 MyMeta 的 __call__ 运算符重载。
        class = type(classname, superclasses, attributedict)
        # 变为了
        class = MyMeta(classname, superclasses, attributedict)
"""
class Mymeta(type):
    def __init__(self, name, bases, dic):
        """
        当你定义一个类时，写成下面这样时：
            class MyClass:
                data = 1
        Python 真正执行的是下面这段代码：
            class = type(classname, superclasses, attributedict)
            这里等号右边的 type(classname, superclasses, attributedict)，就是 type 的 __call__ 运算符重载，它会进一步调用:
            type.__new__(typeclass, classname, superclasses, attributedict)
            type.__init__(class, classname, superclasses, attributedict)
        """
        super().__init__(name, bases, dic)
        print('===>Mymeta.__init__')
        print(self.__name__)
        print(dic)
        print(self.yaml_tag)

    def __new__(cls, *args, **kwargs):
        print('===>Mymeta.__new__')
        print(cls.__name__)
        return type.__new__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('===>Mymeta.__call__')
        obj = cls.__new__(cls)
        cls.__init__(cls, *args, **kwargs)
        return obj


class Foo(metaclass=Mymeta):
    yaml_tag = '!Foo'

    def __init__(self, name):
        print('===>Foo.__init__')
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('===>Foo.__new__')
        return object.__new__(cls)


if __name__ == '__main__':
    foo = Foo('foo')
    for i in range(10):
        foo=type(foo)
        print(foo)
