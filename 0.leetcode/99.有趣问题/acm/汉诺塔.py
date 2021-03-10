#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
def move(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        move(n-1,x,z,y)
        print(x,'-->',z)
        move(n-1,y,x,z)
def main():
    n=5
    move(n,'1','2','3')
main()