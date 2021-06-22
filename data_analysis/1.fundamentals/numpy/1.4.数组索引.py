import numpy as np
arr=np.arange(10)
#1.切片（不复制数据，直接改变原数据）
arr[2:7]=10
arr[:2]=1
arr[7:]=2
print(arr)
arr[:]=np.arange(10)
#2.多维数组索引(原表的视图，无复制，会改变数据）
arr=np.arange(64).reshape(8,8)
#以下两种索引方式完全相同，三维的时候就多个逗号
#索引一个值
print(arr[3,3])
print(arr[3][3])
#索引表中表
print(arr[3:,3:])
#3.布尔索引(原表的视图，无复制,会改变数据）
names=np.array(['bob','joe','will','bob','will','joe','joe'])

data=np.arange(28).reshape(7,4)
bool_arr=(names=='bob')
print(bool_arr)
print(data[bool_arr])  #只取true的部分
#改变一下数据
data[bool_arr]=1
print(data)

#4.fancy index(花式索引）传入的是数组 (原数组的copy，不会改变原数组）
print(data[[0,5]])
arr=data[[0,5]]
#并不会改变原数组
arr[:]=2
print(arr)
print(data)
