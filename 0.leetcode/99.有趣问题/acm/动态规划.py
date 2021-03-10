#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
weight_value=[                                              #第一个是weight，第二个是value
    [2,3],[1,2],[3,4],[2,2]
]
def solve(maxweight):
    arr=np.zeros((len(weight_value)+1,maxweight))
    for i in range(len(weight_value)):
        for  j in range(maxweight):
            if j<weight_value[i][0]:
                arr[i+1,j]=arr[i,j]
            else:
                arr[i+1,j]=max(arr[i,j],arr[i,j-weight_value[i][0]]+weight_value[i][1])
    return arr
print (solve(6))


#--------------------------------------------------------自己的版本
# def dynamic_programming(arr,maxweight):
#     dynamic_table=np.zeros((len(arr)+1,maxweight+1))
#     for i in range(len(arr)):           #前面商品带不带
#         for j in range(maxweight+1):          #后面商品带不带
#             if j <arr[i][0]:
#                 dynamic_table[i+1][j]=dynamic_table[i][j]
#             else:
#                 dynamic_table[i+1][j]=max(dynamic_table[i][j],dynamic_table[i][j-arr[i][0]]+arr[i][1])
#     print(dynamic_table)
# dynamic_programming(weight_value,5)
# [[ 0.  0.  0.  0.  0.  0.]
#  [ 0.  0.  3.  3.  3.  3.]
#  [ 0.  2.  3.  5.  5.  5.]
#  [ 0.  2.  3.  5.  6.  7.]
#  [ 0.  2.  3.  5.  6.  7.]]