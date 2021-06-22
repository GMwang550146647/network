import numpy as np
#1.np.unique返回一个不重复的集合，并排好序
names=np.array(['bob','joe','will','bob','will','joe','joe'])
names_unique=np.unique(names)
print(names_unique)
#相当于 sorted(set(names))
#2.np.intersect1d(x,y) 计算x,y中的公共元素，并返回有序集合
#3.np.union1d(x,y)    计算x,y中的并集，并返回 结果
#4.in1d(x,y)          计算y是否包含x
#5.serdiff1d(x,y)     集合的差，在x中且不在y中的
#6.setxor1d(x,y)      集合的对称差，不同时存在于两个数组中的元素， 即 并集-交集