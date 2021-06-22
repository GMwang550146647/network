'''
__init__.py 文件：
导入包的时候默认调用__init__.py文件
作用：
1.导入该包的时候，把一些初始化的函数，变量，类定义在__init__.py中
2.此文件的变量访问只需要通过import packageAA as pk  就可以继续调用 pk.c
'''

c=100000000
def func():
    print("In pavkageAA func()")

