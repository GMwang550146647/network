'''

特殊方法不需要自己调用，会自己执行
在api 3.data_model的Special method names
'''
class Person:
    def __init__(self,name,age):
        self.arr=[1,2,3,4,5]
        self.name=name
        self.age=age
        self.dict1={}
    '''特殊方法：其实就是print函数的多态，调用对象的__str__()方法或者__repr__()方法'''
    '''1.1__str__:打印的结果'''
    def __str__(self):
        return "str:Person [name=%s,age=%d]" % (self.name, self.age)
    '''1.2.交互模式下打印的结果，带引号'''
    def __repr__(self):
        return "repr:Person [name=%s,age=%d]"%(self.name,self.age)
    '''2.大小比较'''
    # object.__lt__(self, other)
    # object.__le__(self, other)
    # object.__eq__(self, other)
    # object.__ne__(self, other)¶
    # object.__gt__(self, other)
    # object.__ge__(self, other)
    def __eq__(self,other):
        if self.age==other.age:
            return True
        else:
            return False
    '''3.bool值使用'''
    def __bool__(self):
        if self.age>18:
            return True
        else:

            return False
    '''4.加减乘除与非和等运算'''
    # object.__add__(self, other)
    # object.__sub__(self, other)
    # object.__mul__(self, other)
    # object.__matmul__(self, other)
    # object.__truediv__(self, other)
    # object.__floordiv__(self, other)
    # object.__mod__(self, other)
    # object.__divmod__(self, other)
    # object.__pow__(self, other[, modulo])
    # object.__lshift__(self, other)
    # object.__rshift__(self, other)
    # object.__and__(self, other)
    # object.__xor__(self, other)
    # object.__or__(self, other)
    def __add__(self, other):
        return self.name+other.name
    '''
    5.重定义特殊符号：[]
    '''
    def __getitem__(self,index):
        return self.arr[index]

    '''
    6.设置值：__setitem__
     a[key]=value访问方式
    '''
    def __setitem__(self, key, value):
        self.dict1[key]=value

    '''
    7.__iter__:迭代，用于for item in class:
    '''
    def __iter__(self):
        for i in self.arr:
            yield i
    '''
    8.__contains__:包含 用于xx in class
    '''
    def __contains__(self, item):
        if item in self.dict1:
            return True
    '''
    9.__delitem__:删除对象
    '''
    def __delitem__(self, key):
        del self.dict1[key]

'''1.打印多态'''
p1=Person("gm1",20)
p2=Person("gm2",12)
print(p1)
print(repr(p1))
'''2.大小比较多态'''
print(p1==p2)

'''3.bool值使用'''
print(bool(p1)) #强制类型转换也行
if p1:
    print("已成年")
else:
    print("未成年")

'''4.加减乘除运算'''
print(p1+p2)

'''5.重定义index[]'''
print(p1[1])

'''6.设置值'''
p1['a']=999
print(p1.dict1)

'''7.迭代'''
for i in p1:
    print(i)

'''8.包含'''
print("a" in p1)

'''9.删除'''
del p1['a']
print(p1.dict1)
