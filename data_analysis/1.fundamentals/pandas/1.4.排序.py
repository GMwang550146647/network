from pandas import Series,DataFrame
import pandas as pd
#1.创建DataFrame
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'year':[2000,2001,2002,2003,2003],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=DataFrame(data)

#1.对列索引排序（axis=1,ascending是升序）
result=frame.sort_index(axis=1,ascending=False)
print(result)
#2.根据值进行排序,按照年份排序
result=frame.sort_values(by='year')
print(result)