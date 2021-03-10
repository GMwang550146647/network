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
    def min_supp_tree(self):
        length=len(self.matrix)
        list_dist_way=[]
        for i in range(length):
            for j in range(length):
                if self.matrix[i,j]!=0 and self.matrix[i,j]!=100000:
                    list_dist_way.append([self.matrix[i,j],[i,j]])
        list_dist_way.sort(key=lambda x:x[0])  #或者list_dist_way=sorted(list_dist_way,key=lambda x: x[0])
        list_result_dist_way_point=[]
        list_result_dist_way_point=list(list_dist_way[0])
        list_result_dist_way_point.append([list(list_dist_way[0][1])])
        print(list_result_dist_way_point)
        i=0
        while(len(list_dist_way)>0):
                if list_dist_way[i][1][0] in list_result_dist_way_point[1] and list_dist_way[i][1][1] in list_result_dist_way_point[1]:         #两个点都在
                    list_dist_way.pop(i)

                elif list_dist_way[i][1][0] in list_result_dist_way_point[1] and list_dist_way[i][1][1] not in list_result_dist_way_point[1]:   #一个点在
                    list_result_dist_way_point[1].append(list_dist_way[i][1][1])
                    list_result_dist_way_point[2].append(list_dist_way[i][1])
                    list_result_dist_way_point[0]+=list_dist_way[i][0]
                    list_dist_way.pop(i)
                    i=0
                elif list_dist_way[i][1][0] not in list_result_dist_way_point[1] and list_dist_way[i][1][1] in list_result_dist_way_point[1]:   #一个点在
                    list_result_dist_way_point[1].append(list_dist_way[i][1][0])
                    list_result_dist_way_point[2].append(list_dist_way[i][1])
                    list_result_dist_way_point[0]+=list_dist_way[i][0]
                    list_dist_way.pop(i)
                    i=0
                else:                                                                                                                              #都不在
                    i+=1
                print(list_result_dist_way_point)
graph1=graph(arr)
graph1.min_supp_tree()