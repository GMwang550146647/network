# #-*- coding:utf-8 -*-
# import numpy as np
# import pandas as pd
# import sklearn
# from pandas import DataFrame, Series
# import matplotlib.pyplot as plt
# def move(n,x,y,z):
#     if n==1:
#         print(x,'->',z)
#     else:
#         move(n-1,x,z,y)
#         print(x,'->',z)
#         move(n-1,y,x,z)
# move(3,1,2,3)
# arr=[]
# n=8
# x=[0 for i in range(n+1)]
# def check(x,k):
#     for i in range(1,k):
#         if abs(x[k]-x[i])==abs(k-i) or x[k]==x[i]:
#             return False
#     return True
# def n_queen(k):
#     if k>n:
#         arr.append(x)
#     else:
#         for i in range(1,n+1):
#             x[k]=i
#             if check(x,k):
#                 n_queen(k+1)
# n_queen(1)
a=range(10)
print(a)
print(range(10))