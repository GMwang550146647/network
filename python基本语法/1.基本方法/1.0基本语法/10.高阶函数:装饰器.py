


'''
装饰器：给函数增加新功能
注意：在不改变原函数的前提下对函数进行拓展
一般格式：
1.传入函数参数
2.函数中创建函数并输出函数参数
作用：
1.不改变函数源代码的前提下，增添新功能
'''
def deco(func):
    def f(a,b):
        print("计算前")
        result=func(a,b)
        print(result)
        print("已输出")
    return f
@deco
def add(a,b):
    return a+b
@deco
def multiply(a,b):
    return a*b

'''1.旧版本的装饰器（要自己写）'''
# newadd=deco(add)
# newadd(10,20)
# newmultiply=deco(multiply)
# newmultiply(10,20)
print("--------------------")
'''2.加了deco之后的，自动装饰（deco函数一定要在原函数之前定义）'''
add(1,2)
multiply(2,3)


