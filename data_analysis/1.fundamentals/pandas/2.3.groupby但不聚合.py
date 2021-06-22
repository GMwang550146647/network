from pandas import Series,DataFrame
import pandas as pd
import numpy as np
'''任务1'''
#读入两个文件
dfPrice=pd.read_csv('Price.csv',na_values=np.nan)
dfVolume=pd.read_csv('Volume.csv',na_values=np.nan)
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

#分组之后除了聚合还能做很多东西，例如不同的组的数据要进行不同的运算,例如不同组的人的工资要按业绩进行各自的计算

d={'Chevy Cruze':2,'Ford Focus':4,'HONDA CIVIC':10}
def func(df,d):
    print(df)
    return d[df.values[0,0]]*df
grouped_class=join_pv[['class','Price','Volume']].groupby('class')
grouped_result=grouped_class.apply(func,d=d)  #如果是自定义的函数不需要加引号
print(grouped_result)