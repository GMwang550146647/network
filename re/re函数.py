#-*- coding:utf-8 -*-
import re
'''1.search函数'''
search=re.search(r'[1-9]\d{5}','BIT 100081')
if search:
    print(search.group(0))
    print(search.span())
    
'''2.match函数,从头位置开始匹配'''
match=re.match(r'[1-9]\d{5}','BIT 100081')
if match:
    print (match.group(0))
    print(match.span())
else:
    print('fail')

'''3.findall函数,返回所有'''
ls=re.findall(r'\d{5}','3809480948')
print (ls)

'''4.split函数,分割结果'''
ls=re.split(r'[1-9]\d{5}','BIT 100081 TSU100084gmm')
print (ls)
ls=re.split(r'[1-9]\d{5}','BIT 100081 TSU100084gmm',maxsplit=1)
print (ls)

#特殊：要是加个括号就不会删除分隔符
result=re.split('([\+\*-/])','45+3*7332-22/33')
print(result)

'''5.finditer函数'''
for item in re.finditer(r'[1-9]\d{5}','BIT 100081 TSU100084'):
    if item:
        print (item)

'''6.sub函数'''
result=re.sub(r'[1-9]\d{5}','gm','BIT 100081 TSU100084')
print(result)


