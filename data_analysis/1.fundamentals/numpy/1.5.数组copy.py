import numpy as np
import copy
###################################################
#对于numpy数组来说，deepcopy和copy一样
#1.浅copy只能copy到一维数组级别
#2.深copy用于copy多维数组

arr=np.arange(27).reshape(3,3,3)
arr_copy=copy.copy(arr)
arr_deepcopy=copy.deepcopy(arr)
arr_npcopy=arr.copy()
arr[0]=1
print(arr_copy)
print(arr_deepcopy)
print(arr_npcopy)
###################################################
#对于python自带的数组不是：
import copy

a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象
b = a  # 赋值，传对象的引用,算是别名，两者指向一样
c = copy.copy(a)  # 对象拷贝，浅拷贝 由于c[5]和a[5]一样只是指向新数组的地址，所以改变a，c（浅copy）也会变
d = copy.deepcopy(a)  # 对象拷贝，深拷贝
a.append(5)  # 修改对象a
a[4].append('c')  # 修改对象a中的['a', 'b']数组对象
print(a)
print(b)
print(c)
print(d)
# a = [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# b = [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# c = [1, 2, 3, 4, ['a', 'b', 'c']]
# d = [1, 2, 3, 4, ['a', 'b']]