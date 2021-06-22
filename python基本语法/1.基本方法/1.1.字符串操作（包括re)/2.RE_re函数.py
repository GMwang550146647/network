#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import re
#search函数
match=re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print (match.group(0))
#match函数,从头位置开始匹配
match=re.match(r'[1-9]\d{5}','BIT 100081')
if match:
    print (match.group(0))
else:
    print('fail')
#findall函数,返回所有
ls=re.findall(r'[1-9]\d{5}','BIT 100081 TSU100084')
print (ls)
#split函数,分割结果
ls=re.split(r'[1-9]\d{5}','BIT 100081 TSU100084gmm')
print (ls)
ls=re.split(r'[1-9]\d{5}','BIT 100081 TSU100084gmm',maxsplit=1)
print (ls)
#finditer函数
for item in re.finditer(r'[1-9]\d{5}','BIT 100081 TSU100084'):
    if item:
        print (item)
#sub函数
result=re.sub(r'[1-9]\d{5}','gm','BIT 100081 TSU100084')
print(result)