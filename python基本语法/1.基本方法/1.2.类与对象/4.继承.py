class Animal:
    def __init__(self,place):
        self.place=place
    def run(self):
        print("动物会跑")
    def sleep(self):
        print("动物会睡觉")
class Dog(Animal):
    def __init__(self,place,like):
        '''0.就连__init__函数也会被继承，自己重写会把父类的覆盖，所以要先调用一下父类的'''
        # Animal.__init__(self,place)
        super().__init__(place) #与上一句完全相同意思，而且不需要调用self，super()的意思是父类
        self.like=like
    def sleep(self):
        print("狗会睡觉")
    def bark(self):
        print("狗会叫")

'''
继承：
不用重定义相同的函数，减少代码量
(默认继承自object）
'''
'''0.就连__init__函数也会被继承，自己重写会把父类的覆盖，所以要先调用一下父类的'''
dog1=Dog("地球","喜欢睡觉")
'''1.run继承自Animal类，如果当前类没有该方法，则去父类中寻找'''
dog1.run()
'''2.sleep是自己的（子类方法重写），如果当前类有该方法，就在本类中寻找'''
dog1.sleep()
'''3.bark是狗类特有的'''
dog1.bark()

#4.类型判断
print("检查dog1是否dog实例:",isinstance(dog1,Dog))
print("检查dog1是否animal实例：",isinstance(dog1,Animal))
print("检查dog是否animal子类：",issubclass(Dog,Animal))