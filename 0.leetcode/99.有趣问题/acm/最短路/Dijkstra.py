#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
arr=[
[0,20,np.inf,np.inf,10,np.inf],
[20,0,7,8,5,np.inf],
[np.inf,7,0,3,np.inf,np.inf],
[np.inf,8,3,0,20,np.inf],
[10,5,np.inf,20,0,2],
[np.inf,np.inf,np.inf,np.inf,2,0]
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
        self.min_way=[np.inf] *len(arr)
        self.matrix=np.array(arr)
        self.node_arr=[]
        self.node_value_arr=[]
        print(self.matrix)
        for i in range(len(self.matrix)):
            self.node_arr.append(node(i))
        for i in range(len(self.matrix)):
            tempt=[]
            for j in range(len(self.matrix[i])):
                if self.matrix[i,j]!=0 and self.matrix[i,j]!=np.inf:
                    tempt.append(j)
            self.node_value_arr.append(tempt)
        for i in range(len(self.node_arr)):
            for j in self.node_value_arr[i]:
                self.node_arr[i].link.append(self.node_arr[j])

    def Dijkstra(self):
        list_dist_fix_way=[]                    #list类型的距离-是否固定-路径
        length=len(self.matrix)
        for i in range(length):
                list_dist_fix_way.append([self.matrix[0,i],0,[0]])
        for i in range(10):             #固定第i个点
            tempt_min=100000;temptj=-1
            find=0
            for j in range(length):             #遍历一次，找出未固定的最小点
                if list_dist_fix_way[j][1]!=1 and list_dist_fix_way[j][0]<tempt_min:
                    tempt_min=list_dist_fix_way[j][0]
                    temptj=j
                    find=1
            list_dist_fix_way[temptj][1]=1
            print(list_dist_fix_way)
            if find==1:
                for k in range(length):
                    if list_dist_fix_way[k][1]==1:
                        continue
                    elif self.matrix[temptj][k]+list_dist_fix_way[temptj][0]<list_dist_fix_way[k][0]:
                        list_dist_fix_way[k][0]=self.matrix[j][k]+list_dist_fix_way[j][0]
                        list_dist_fix_way[k][2]=list(list_dist_fix_way[temptj][2])
                        list_dist_fix_way[k][2].append(temptj)
            else:
                continue

        print(list_dist_fix_way)
graph1=graph(arr)
graph1.Dijkstra()

