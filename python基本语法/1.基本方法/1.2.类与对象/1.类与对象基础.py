#执行顺序
#1.创建一个变量
#2.内存中创建一个新对象
#3.执行类代码块中的代码（只在类中定义），例如下面的"name1='gmwangPublic'"
#4.__init__(self)方法执行
#5.将对象id赋值给变量


class Student():
    #定义该对象的方法，这个是各个类共享的（也就是每个类都能修改）
    name1='gmwangPublic'
    #特殊方法（带__开头和结尾的），不需要自己调用，__init__函数是构建函数
    def __init__(self,name="gmwangSelf"):
        #这个name是每个对象各自不同的name
        self.name=name
    def getName(self):
        print(self.name1)

s1=Student()
#类外可以定义该对象的附加属性
s1.name2='gmwang'
print(s1.name2)
#调用类的属性和方法
s1.getName()
print(s1.name1)

print(isinstance(s1,Student))