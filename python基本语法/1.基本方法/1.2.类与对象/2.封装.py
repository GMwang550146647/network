
'''
封装：隐藏对象中不希望被外部使用的属性和方法
1.隐藏属性名，无法随意修改属性
2.添加get，set函数，可以令变量只读或者只写等
3.使用set函数令属性数据格式正确

'''

'''1.方法1：使用双下划线"__",但是一般不用'''
class Person():
    def __init__(self,name):
        self.__name=name
    def setName(self,newname):
        self.__name=newname
    def getName(self):
        return self.__name
p1=Person('gmwang');
# print(p1.__name)  #这个报错，提示没有这个属性，但是
print(p1._Person__name) #但是通过这个也能访问

'''2.方法2：使用单下划线"_"(一般用这个)'''
class Person2():
    def __init__(self,name):
        self._name=name
    def setName(self,newname):
        self._name=newname
    def getName(self):
        return self._name

p2=Person2('gmwang');
print(p2._name)