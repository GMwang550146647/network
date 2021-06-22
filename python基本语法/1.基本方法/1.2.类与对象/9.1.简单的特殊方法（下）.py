import sys
class Person:
    '''1.__init__:初始化方法'''
    def __init__(self,name):
        print("init")
        self.name=name
    '''
    2.__new__:实例化方法
    作用：
    1.新建一块内存空间，返回一个地址给__init__()

    '''
    def __new__(cls,*args,**kwargs):
        print("new")
        position=super(Person,cls).__new__(cls)
        print(position)
        return position
    '''
    3.__call__:把实例对象当成函数用
    作用：objname（）的时候用
    '''
    def __call__(self, *args, **kwargs):
        print('call')
    '''
    4.__del__:析构函数：请不要用，仅供理解，因为自己定义大概率会导致内存泄漏
    作用：当该对象在没有引用（或者是程序末尾）会删除该对象（垃圾回收机制）
    '''
    def __del__(self):
        print("self.name已del")
        del self.name
'''测试'''
P=Person("gmwang")
'''3.call测试：'''
P()

'''？.del测试'''
p1=P
del P   #这个del只是删除引用，仍然可以通过p1.name输出该变量
print(p1.name)
print(sys.getrefcount(p1))   #这个函数是获取该对象的引用个数（如果是0会被后台自动处理掉）仍然有一个引用，所以没删除
