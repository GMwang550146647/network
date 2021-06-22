from pandas import Series,DataFrame
import pandas as pd
import numpy as np
'''任务1'''
#读入两个文件
dfPrice=pd.read_csv('Price.csv',na_values=np.nan)
dfVolume=pd.read_csv('Volume.csv',na_values=np.nan)
print(dfPrice)
#表连接操作
join_pv=pd.merge(dfPrice,dfVolume,on=['Vehicle name','year','month'])
#保存连接后的文件
join_pv.to_csv('1.mergeresult.csv')
'''任务2'''
#转化字典，把车的名字归成三类：'Chevy Cruze'，'Ford Focus'，'HONDA CIVIC'
class_dict={
    'Chevy Cruze':'Chevy Cruze',
    'Focus Hatchback':'Ford Focus',
    'Ford Focus Hatchback':'Ford Focus',
    'Ford Focus Sedan':'Ford Focus',
    'HoNDA CiviC':'HONDA CIVIC',
    'Honda Civic':'HONDA CIVIC'
}
join_pv['class']=join_pv['Vehicle name'].map(class_dict)
print(join_pv)

#1.根据class进行分组，分组之后用agg对其进行聚合操作，具体的操作是mean，和count，这两个函数是经过优化的，所以能这样用
grouped_class=join_pv.groupby('class')
grouped_result=grouped_class.agg(['mean','count'])[['Price']]
print(grouped_result)

#2.自定义操作函数,对多列进行groupby
def peak_to_peak(arr):
    return arr.max()-arr.min()
grouped_class=join_pv[['class','Price','Volume']].groupby('class')
grouped_result=grouped_class.agg([peak_to_peak,'mean'])  #如果是自定义的函数不需要加引号
#可以加引号的函数如下所示：
#count,sum,mean,median,std,min,max,prod,describe,last,first
print(grouped_result)

#3.自定义操作函数,对多列进行groupby,每一列的操作函数不一样要传入字典
def peak_to_peak(arr):
    return arr.max()-arr.min()
grouped_class=join_pv[['class','Price','Volume']].groupby('class')
grouped_result=grouped_class.agg({'Price':[np.max,'sum'],'Volume':'mean'})  #每一列的操作函数不一样要传入字典
#可以加引号的函数如下所示：
#count,sum,mean,median,std,min,max,prod,describe,last,first
print(grouped_result)

