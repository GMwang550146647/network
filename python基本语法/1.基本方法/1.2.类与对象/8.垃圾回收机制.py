'''
没有变量引用的对象就是垃圾
'''
class A:
    def __init__(self):
        self.name='A类'
    '''3.__del___是被删除的时候调用的'''
    def __del__(self):
        print("A类被删除了")
'''1.创建的A()由于没被引用了，就被自动回收了'''
a=A()
a=None
'''2.如果还有引用就不被回收'''
a=A()
b=a
a=None
del a
print(b.name)
input('回车键就被回收')
