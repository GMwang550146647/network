'''1.初始化和提取值'''
d = {'a': 1, 'b': 2, 'c': 3}
for value in d.values():
    print(value)
for key in d.keys():
    print(key)
for k, v in d.items():
    print(k,":",v)


'''2.删除键值对'''

#2.1.删除一个
# del d['a']
print(d.pop('d','没有此值'))    #删除成功返回a对应的value：1，删除不成功报keyError，但是加入个默认返回值就不报错
print(d)
#2.2.删除全部
d.clear()

'''3.获取键值'''
print(d.get('c','查无此值'))
print(d.get('d','查无此值'))


'''4.有序字典:按加入字典的先后顺序排列'''
import collections
dictOrder=collections.OrderedDict()
dictOrder['1']=1
dictOrder['2']=2
dictOrder['0']=0
print(dictOrder)