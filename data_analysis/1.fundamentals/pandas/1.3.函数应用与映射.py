from pandas import Series,DataFrame
import pandas as pd
#1.创建DataFrame
data={
      'year':[2000,2001,2002,2003,2003],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=DataFrame(data)
print(frame)
#1.frame.apply(func)  其实就是把frame看作是一个一个的Series元素，逐个丢进去函数里面计算
result=frame.apply(lambda x: x.max()-x.min(),axis=0)  #axis=0意思是每一列对应的最大值和最小值相减，合成一行
print(result)
#1.1.新建一个特征，由其他特征计算得到
# df['petal area'] = df.apply(lambda r: r['petal length'] * r['petal width'],axis=1)  #axis=1意思是增添一列

#1.2.传入函数和参数
def func(x):
      return x['year']-x['pop']
result=frame.apply(func,axis=1)
print(result)

#2.frame.applymap(func)  对frame的每一个数进行该操作
result=frame.applymap(lambda x:x**2)
print(result)

#3.series.map()
series=frame['year']
result=series.map(lambda x:x**4)
print(result)
