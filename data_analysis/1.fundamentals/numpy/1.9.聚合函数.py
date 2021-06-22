import numpy as np
arr=np.arange(100).reshape(10,10)
#1.平均数
mean1=arr.mean(1)#第1维度聚合的平均数
mean0=arr.mean(0)#第0维度聚合的平均数
mean=arr.mean()  #整个数组的平均数
print(mean1)
print(mean0)
print(mean)
#2.求和
sum1=arr.sum(1)
sum0=arr.sum(0)
sum=arr.sum()
print(sum1)
print(sum0)
print(sum)

#3.累计求和
sum1=arr.cumsum(1) #向横求和
sum0=arr.cumsum(0) #向纵求和
sum=arr.cumsum()    #一个一个求和
print(sum1)
print(sum0)
print(sum)

#4.标准差
# std(或var）标准差，自由度可以调整，默认为n
#5.最大最小
# min,max
#6.最大最小编号
# argmin ,argmax（返回最大最小的索引编号）
#7.累积积
# cumprod 累计积