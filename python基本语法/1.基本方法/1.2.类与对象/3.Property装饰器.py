class Person():
    def __init__(self,name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newname):
        self.__name = newname

p2=Person('gmwang')

'''
1.使用@property装饰器之后就不需要再用：
p2.name()
只需要
p2.name
这样就像是属性一样调用就行了

'''
print(p2.name)
'''
2.使用name.setter装饰器之后只需要
P2.name=xxx就行了
'''
p2.name="gmwnagwangwang"
