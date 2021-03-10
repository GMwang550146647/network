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
    def  TopuSort(self):
