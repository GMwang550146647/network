#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
def ratio_search(arr,num):
    print('i')
    mid=int(num/float(arr[-1]-arr[0])*(len(arr)-1))
    if len(arr)==0:
        print('FAIL')
    if num==arr[mid]:
        print('FIND')
    elif num<arr[mid]:
        ratio_search(arr[:mid],num)
    else:
        ratio_search(arr[mid+1:])

ratio_search(range(50),10)