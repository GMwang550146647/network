
class A:
    def __init__(self,name):
        self._name=name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name
class B:
    def __init__(self,name):
        self._name=name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name
a=A("gma")
b=B("gmb")
'''
1.多态：不同的类调用其各自同名函数，不同类有不同的操作方法，这就是多种形态

'''
def say_hello(obj):
    print("你好",obj.name)
say_hello(a)
say_hello(b)

'''
2.关于len()函数:之所以能实现多态，是因为其拥有方法"__len__"，见以下的C类例子
'''
l=[1,2,3,4]
s="hello"
print(len(s))
print(len(l))
#
class C:
    def __len__(self):
        return 10
c=C()
print(len(c))