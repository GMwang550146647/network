from pandas import Series,DataFrame
import pandas as pd
#1.创建DataFrame
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'year':[2000,2001,2002,2003,2003],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=DataFrame(data)
#2.创建DataFrame并指定顺序
frame=DataFrame(data,columns=['year','pop','state'])

#3.索引
#3.1.列索引
print(frame['pop'])
#3.2.自由索引,index 为3，column为'year'的列
print(frame.loc[3,'year'])
#3.3.

#4.属性
#4.1.columns ：列索引
print(frame.columns)
#4.2.index :行索引
print(frame.index)
#4.3.values :numpy.array
print(frame.values)
#4.4.


# 5.转置:行变列，列变行
print(frame.T)

#6.重新索引
frame_tran=frame.reindex(index=[4,3,2,1,0],columns=['state','pop','year'])
print(frame_tran)

#7.丢弃某些指定轴上的项(不改变原来的frame),可指定axis,1为列，0为行
frame_droped=frame.drop(['pop','year'],axis=1)
print(frame_droped)
