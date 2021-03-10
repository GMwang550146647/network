#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
p=20
p_to_release=[2,5,14]
prisoner=[i for i in range(20)]
money=0
path=[]
def bribe(p_to_release,prisoner,left=0,right=19,i=0):
    i+=1
    if len(p_to_release)<=0:
        return 0
    if len(p_to_release)==1:
        return len(prisoner)-1
    global money
    global path
    money+=len(prisoner)-1
    for p in range(len(p_to_release)):
        path.append(p_to_release[p])
        release_group_left=p_to_release[:p]
        release_group_right=p_to_release[p+1:]
        prisoner_group1_left=left
        prisoner_group1_right=p_to_release[p]
        prisoner_group2_left=p_to_release[p]+1
        prisoner_group2_right=right
        temptmoney1=bribe(release_group_left,prisoner,prisoner_group1_left,prisoner_group1_right,i)
        temptmoney2=bribe(release_group_right,prisoner,prisoner_group2_left,prisoner_group2_right,i)
        money+=temptmoney1+temptmoney2
        if i ==1:
            print(money)
            print(path)
            path=[]
            money=0
    return float(money)
print(bribe(p_to_release,prisoner))