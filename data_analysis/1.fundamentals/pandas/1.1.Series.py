from pandas import Series,DataFrame
import pandas as pd
#1.创建Series（定长有序的字典）
obj=Series([1,2,3,4,56,6])
print(obj)
#2.多了一个属性：可自由指定的index
obj=Series([1,2,3,4,56,6],index=['a','b','c','d','e','f'])
print(obj)
#3.series的属性
print(obj.index)
print(obj.values)
#4.重新索引:并不会改变列表本身
objk=obj.reindex(['f','e','d','c','b','a','x'])
print(objk)
#5.