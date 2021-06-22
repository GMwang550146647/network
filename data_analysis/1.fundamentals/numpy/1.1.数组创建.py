import numpy as np
#1.利用list创建数组
list1=[1,2,3,4,5,6,7,8,9,10]
arr1=list(list1)
print(arr1)
#2.全1
arr2=np.ones((10,10))
print(arr2)
#3.全0
arr3=np.zeros((10,10))
print(arr3)
#4.空值,不推荐使用，因为没用
arr4=np.empty((2,3))
print(arr4)
#5.等差数列
arr5=np.arange(20) #0-19
arr5=np.arange(10,100,5)  #从10 到100，间隔是5
print(arr5)
#6.NXN单位矩阵（对角线为1，其余为0）
arr6=np.eye(10)
#arr6=np.identity(10)  #同上
print(arr6)

#7.利用reshape改变数组姓朱那个
arr7=np.arange(100).reshape((10,10))
print(arr7)

#8.网格数据(相当于生成  x∈【-5，5】，y∈【-5，5】的一个正方形的点集
points=np.arange(-5,5,0.1)
xs,ys=np.meshgrid(points,points)
print(xs)
print(ys)