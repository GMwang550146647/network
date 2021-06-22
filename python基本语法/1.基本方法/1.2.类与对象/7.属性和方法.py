class A(object):
    '''1.类属性，通过实例或者类都能调用,但是只能通过类对象修改，不能通过实例属性修改'''
    count=0
    def __init__(self,name="gmwang"):
        '''3.实例属性：只能通过实例对象访问，不能通过类对象访问'''
        self.name=name
    '''4.实例方法'''
    def test(self):
        print("这个是test方法~~~：",self)
    '''2.类方法'''
    @classmethod
    def test_2(cls):
        print("这个是类方法：",cls)
        print(cls.count)
    '''5.静态方法：不需要任何参数（self or cls)，与该类无关，只是找个位置放下而已'''
    @staticmethod
    def test_3():
        print("test_3执行了，静态方法")
        print(A.count)

'''1.类属性，通过实例或者类都能调用,但是只能通过类对象修改，不能通过实例属性修改'''
a=A()
a.count=100
print("A.count:",A.count)
print("a.count:",a.count)
a1=A()
#如果实例'修改'类属性，仅是新政了一个属性，不再是类属性了，调用时只会调用自己的属性，不会修改类属性
a1.count=999
A.count=100
print("A.count:",A.count)
print("a.count:",a1.count)

'''2.类方法（一般不用）:与实例方法的区别：前者第一个参数是cls，后一个是self,不能使用self的属性
特点：
1.依赖装饰器@classmethod
2.参数是cls不是self
3.只可以使用类方法，类属性
作用：
1.创建对象之前完成一些动作
'''
A.test_2()
a.test_2()

'''3.实例属性：只能通过实例对象访问，不能通过类对象访问'''
a=A()
# print(A.name)  #报错，不能
print(a.name)

'''4.实例方法:以下两种方法一样，'''
# A.test()  #该方法会报错
A.test(a)
a.test()


'''5.静态方法
特点：
1.需要装饰器
2.不能使用实例方法，属性 （可以使用类方法，类属性）
3.与类方法类似，唯一区别是没有cls参数，以及调用类属性的时候要用A.xxx

'''
A.test_3()
a.test_3()