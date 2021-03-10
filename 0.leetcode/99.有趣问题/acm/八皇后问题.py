#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
#检查是否有上下左右斜线相交
def check(a,n):
    for i in range(1,n):
        if(abs(a[i]-a[n])==abs(i-n)) or (a[i]==a[n]):
            return False
    return True
n=8
arr=[]
x=[0 for i in range(n+1)]
#递归（补平衡树，若不符合条件，提前结束）
def n_queen(k):
    if k>n:
        arr.append(x)
    else:
        for i in range(1,n+1):
            x[k]=i
            if check(x,k):
                n_queen(k+1)
        return
n_queen(1)
print(len(arr))

