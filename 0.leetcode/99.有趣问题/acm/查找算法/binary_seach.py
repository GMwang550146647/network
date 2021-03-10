#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import time
y=0
def binary_search(arr,x):
    print('i')
    global y
    if len(arr)<=0:
        print('fail')
    middle=int(len(arr)/2)
    if arr[middle]==x:
        print('FIND')
        return
    else:
        if x>arr[middle]:
            binary_search(arr[middle+1:],x)
        else:
            binary_search(arr[:middle],x)
binary_search(range(50),9)
# def search1(arr,m):   #寻找加起来等于m的四个数
#     len_arr=len(arr)
#     result=[]
#     for i in range(len_arr):
#         for j in range(len_arr):
#             for k in range(len_arr):
#                 left=m-i-j-k
#                 binary_search(arr,left)
#                 if y==True:
#                     result.append([i,j,k,left])
#     return result
# def search2(arr,m):
#     len_arr=len(arr)
#     result=[]
#     for i in range(len_arr):
#         for j in range(len_arr):
#             for k in range(len_arr):
#                 for l in range(len_arr):
#                     if i+j+k+l==m:
#                         result.append([i,j,k,l])
#     return result
# arr=range(110)
# start_time=time.clock()
# search1(arr,100)
# print 'time:',time.clock()-start_time
# start_time=time.clock()
# search2(arr,100)
# print 'time:',time.clock()-start_time