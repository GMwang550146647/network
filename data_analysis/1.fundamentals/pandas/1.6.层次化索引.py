from pandas import Series,DataFrame
import pandas as pd
import numpy as np
#读入两个文件
dfPrice=pd.read_csv('Price.csv',na_values=np.nan)
dfVolume=pd.read_csv('Volume.csv',na_values=np.nan)

#表连接操作
join_pv=pd.merge(dfPrice,dfVolume,on=['Vehicle name','year','month'])

grouped_class=join_pv.groupby('Vehicle name')
grouped_result=grouped_class.agg(['mean','count'])[['Price']]

# grouped_result.to_csv('2.agg_mean_sum.csv')




#1.unstack
result=grouped_result.unstack()
# print(result)
#2.stack
result=grouped_result.stack()
# print(result)

#3.索引
result=grouped_result.loc[:,'Price'].loc[:,'mean']
print(result)