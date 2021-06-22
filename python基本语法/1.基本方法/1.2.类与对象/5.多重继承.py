'''
（建议：如果没有特殊情况，不要使用）
隐藏属性：__bases__ 当前类的所有父类


'''
class A(object):
    def test(self):
        print("A中的test")
class B(object):
    def test(self):
        print("B中的test")
    def test2(self):
        print("BBB")
'''1.多重继承会使子类拥有多个父类，并会获取所有父类属性'''
class C(A,B):
    pass

class D(A,B,C):
    pass
c1=C()
'''2.如果父类之间有重载函数，优先选择前面的父类(也就是覆盖后面的)，例如这里A在B前'''
c1.test()

'''3.'''