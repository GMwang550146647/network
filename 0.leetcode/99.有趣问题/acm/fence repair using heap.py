#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
class heap(object):
    def __init__(self):
        self.arr=np.zeros(20)
        self.size=0
    def push(self,value):
        position=self.size
        self.size+=1
        while(position>0):
            parent=(position-1)/2
            if self.arr[parent]<=value:
                break
            self.arr[position]=self.arr[parent]
            position=parent
        self.arr[position]=value
    def pop(self):
        min=self.arr[0]
        x=self.arr[self.size-1]
        self.size-=1
        p=0
        while(p*2+1<self.size):
            left=p*2+1
            right=p*2+2
            if self.arr[left]>self.arr[right] and right<=self.size:
                left,right=right,left
            if self.arr[left]>=x:
                break
            self.arr[p]=self.arr[left]
            p=left
        self.arr[p]=x
        return min


def main():
    heap1=heap()
    total=0
    arr=[3,4,5,1,2]
    for i in arr:
        heap1.push(i)
    while(heap1.size>1):
        min1=heap1.pop()
        min2=heap1.pop()
        tempt=min1+min2
        total+=tempt
        heap1.push(tempt)
    print total
