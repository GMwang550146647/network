from pandas import Series,DataFrame
import pandas as pd
import numpy as np
#读入两个文件
dfPrice=pd.read_csv('Price.csv',na_values=np.nan)
dfVolume=pd.read_csv('Volume.csv',na_values=np.nan)

#1.表连接：表连接操作,参数：left,right,on(join的列),如果左右两个表的列名称不一样，可以使用 left_on=[xx,xx...],right_on=[xx,xx...]，如果要用index作为join的对象，left_index,right_index设为True，suffix设置后缀，默认是"_x"，例如suffix=('_left',"_right")

join_pv=pd.merge(dfPrice,dfVolume,on=['Vehicle name','year','month'],how='left')
grouped_class=join_pv.groupby('Vehicle name')
grouped_result=grouped_class.agg(['mean','count'])[['Price']]

#2.表合并（增加行）
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'year':[2000,2001,2002,2003,2003],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=DataFrame(data)
result=pd.concat([frame,frame],axis=0)  #默认axis=0,因为一般只会添加行
print(result)