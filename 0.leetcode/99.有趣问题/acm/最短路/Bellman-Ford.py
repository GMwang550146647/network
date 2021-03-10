#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
arr=[
[0,20,100000,100000,10,100000],
[20,0,7,8,5,100000],
[100000,7,0,3,100000,100000],
[100000,8,3,0,20,100000],
[10,5,100000,20,0,2],
[100000,100000,100000,100000,2,0]
]                                                           #横列是,0到0，1，2,3,4,5,的方向距离！
class node(object):
    def __init__(self,name,value=None,view=0):
        self.name=name
        self.value=value
        self.view=view
        self.link=[]
#邻接矩阵
class graph(object):
    def __init__(self,arr):
        self.min_way=[100000] *len(arr)
        self.matrix=np.array(arr)
        self.node_arr=[]
        self.node_value_arr=[]
        print(self.matrix)
        for i in range(len(self.matrix)):
            self.node_arr.append(node(i))
        for i in range(len(self.matrix)):
            tempt=[]
            for j in range(len(self.matrix[i])):
                if self.matrix[i,j]!=0 and self.matrix[i,j]!=100000:
                    tempt.append(j)
            self.node_value_arr.append(tempt)
        for i in range(len(self.node_arr)):
            for j in self.node_value_arr[i]:
                self.node_arr[i].link.append(self.node_arr[j])
    def Bellman_Ford(self):
        list_list_dist_way=[]
        list_dist_way=[] #第一个元素是距离，第二个距离是路径
        length=len(self.matrix)
        for i in range(length):
            list_dist_way.append([self.matrix[i,0],[0]])
        print(list_dist_way)
        for i in range(length):             #第n次计算d
            for j in range(length):                    #计算到第j个点的短距离
                for k in range(length):       #扫描matrix这个距离矩阵,寻找新的到j的k
                    if self.matrix[k,j]!=100000 and self.matrix[k,j]!=0:
                        if list_dist_way[k][0]+self.matrix[k,j]<list_dist_way[j][0]:
                            list_dist_way[j][0]=list_dist_way[k][0]+self.matrix[j,k]
                            list_dist_way[j][1]=list(list_dist_way[k][1])
                            list_dist_way[j][1].append(k)
                print(list_dist_way)
        min_value1= list([item[0] for item in list_dist_way])
        for i in range(2):             #计算多一次，如果结果不一样就是错误答案
            for j in range(length):                    #计算到第j个点的短距离
                for k in range(length):       #扫描matrix这个距离矩阵,寻找新的到j的k
                    if self.matrix[k,j]!=100000 and self.matrix[k,j]!=0:
                        if list_dist_way[k][0]+self.matrix[k,j]<list_dist_way[j][0]:
                            list_dist_way[j][0]=list_dist_way[k][0]+self.matrix[j,k]
                            list_dist_way[j][1]=list(list_dist_way[k][1])
                            list_dist_way[j][1].append(k)
        min_value2= [item[0] for item in list_dist_way]
        if not min_value2==min_value1:
            print('Fail to solve')
            return False
        print(list_dist_way)
graph1=graph(arr)
graph1.Bellman_Ford()
#[[0, [0]], [15, [0, 4]], [22, [0, 4, 1]], [23, [0, 4, 1]], [10, [0]], [12, [0, 4]]]
#[[0, [0]], [15, [0, 4]], [22, [0, 4, 1]], [23, [0, 4, 1]], [10, [0]], [12, [0, 4]]]