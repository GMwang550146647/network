'''1.map,全部进行同样的函数操作'''
def func(x):
    return x**2
result=map(func,[1,2,3,4,5,6,7,8])
print(result)

'''2.reduce,就是把好多数reduce成一个数（聚合操作，例如求和）'''
# 原理：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x,y):
    return x*10+y
result=reduce(add,[1,2,3,4,5,6,7,8])
print(result)

# 例子：把str转换成int
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
result=reduce(add,map(char2num,'13579'))
print(result)

'''3.filter函数 过滤'''
def is_odd(n):
    return n % 2 == 1

arr=filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
print(list(arr))

'''4.sorted函数'''
#4.1. 默认排序（从小到大）
result=sorted([36, 5, 12, 9, 21])
result_re=sorted([36, 5, 12, 9, 21],reverse=True)
print(result)
print(result_re)
#4.2.传入函数
result_func=sorted([36, 5, 12, 9, 21],key=lambda a:-a,reverse=True)
print(result_func)