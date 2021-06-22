'''可迭代对象'''
from collections import Iterable
'''1.判断是否可迭代'''
#列表
print(isinstance([1,2,3,4,5],Iterable))
#生成器
print(isinstance(range(5),Iterable))

'''
2.迭代器
（只能往前不能往后，从第一个对象到最后一个）
注意：
1.列表不是迭代器！但是是可迭代对象，可以经过iter函数转换成迭代器
2.生成器属于迭代器，但是不等于迭代器
'''
#列表转换迭代器：
iterArr=iter([1,2,3,4,5,6,7])
for i in iterArr:
    print(i)


