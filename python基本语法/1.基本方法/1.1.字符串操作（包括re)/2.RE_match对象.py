#-*- coding:utf-8 -*- 
import numpy as np
import pandas as pd
import sklearn
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import re
match=re.search(r'[1-9]\d{5}','BIT 100081kkk 100086')
print (match.string)
print(match.re)
print(match.pos)
print (match.endpos)
print(match.group(0))
print (match.start())
print(match.end())
print(match.span())