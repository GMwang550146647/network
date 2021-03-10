#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import time
def fib1(n):
    if n<=1:
        return n
    return fib1(n-1)+fib1(n-2)
for i in range(20):
    print fib1(i)

arr=[0,1]
def fib2(n):
    if n<=1:
        return n
    if len(arr)>n:
        return arr[n]
    value=fib2(n-2)+fib2(n-1)  #这一种调用方法比value=fib2(n-1)+fib2(n-2)调用速度快一点
    arr.append(value)
    return value
start=time.clock()
print fib2(500)
print time.clock()-start