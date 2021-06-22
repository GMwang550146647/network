from pandas import Series,DataFrame
import pandas as pd
#1.创建DataFrame
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'year':[2000,2001,2002,2003,2003],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=DataFrame(data)
#1.求和，axis=1(默认）是对列进行求和，skipna默认是True,即na不当一个，而是忽略
result=frame.sum(axis=1,skipna=False)
print(result)
#2.最厉害的
result=frame.describe()
print(result)