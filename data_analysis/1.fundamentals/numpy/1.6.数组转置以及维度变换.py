import numpy as np
#1.数组维度变换
arr=np.arange(15).reshape(3,5)
# arr=np.arange(15).reshape((3,5))#作用同上
#2.数组转置（简易版本）(并不会把原数组反转）(原数组的一个视图，不复制数据，会改变原数据）
arr_T=arr.T
arr_T[2,2]=1000 #会改变原数据
print(arr)
#3.标准版本(并不会把原数组反转）(原数组的一个视图，不复制数据，会改变原数据）
arr_T=arr.transpose(1,0)  #0,1的意思是第一维度在前，第0维度在后
arr_T[2,1]=100000
print(arr)
#4.标准版本（高维度状态）（会改变原数据）
arr=np.arange(24).reshape(2,3,4)
print(arr)
arr_T=arr.transpose(2,1,0)
print(arr_T)