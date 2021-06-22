#随机数生成
import numpy as np
#1.seed 种子
np.random.seed(0)
#2.permutation
arr_perm=np.random.permutation(10) #0-9乱序排列
print(arr_perm)
#3.shuffle
arr=np.array([1,2,3,4,5,6,7,8,9,0])
np.random.shuffle(arr)  #直接改变传入的数组
print(arr)
#4.rand 0-1均匀分布,传入形状就好
arr_rand=np.random.rand(5,5)
print(arr_rand)
#5.randint 0-9的随机整数（维度是5x5)
arr_randint=np.random.randint(0,10,(5,5))
print(arr_randint)
#6.randn  标准正态分布（平均为0，标准差为1），形状为5x5
arr_randn=np.random.randn(5,5)
print(arr_randn)
#7.binomial
#8.normal 正态分布  形状是5x5 平均值为10，标准差为2
arr_normal=np.random.normal((5,5),10,2)
#9.beta
#9.chisquare
#10.gamma
#11.uniform 产生在0-5中的均匀分布(不包括5）
arr_uniform=np.random.uniform(0,5)
print(arr_uniform)