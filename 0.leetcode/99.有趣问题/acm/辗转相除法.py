#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
def get_max_factor(a,b):
    if a<b:
        a,b=b,a
    yushu=1
    while yushu!=0:
        yushu=a%b
        b=a
        a=yushu
    print(b)
get_max_factor(9,6)