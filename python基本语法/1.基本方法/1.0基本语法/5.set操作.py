'''集合'''

'''1.创建集合'''
set1=set([1,2,3,4,4,3,3,2,1])
set2={1,2,5,6,9}
'''2.集合基本操作'''
#2.1.添加
set1.add(100)
#2.2.删除
set1.remove(100)
#2.3.清空
# set1.clear()


'''3.集合运算'''
#3.1.差集（前者有的后者没有的）
setdiff=set1-set2
setdiff1=set1.difference(set2)  #函数模式
print(setdiff)
print(setdiff1)
#3.2.并集（两个集合加起来）
# and操作或者|
setunion=set1|set2
setunion1=set1.union(set2)
print(setunion)
print(setunion1)

#3.3.交集（公共部分）
#&操作& 或者
setintersection=set1&set2
setintersection1=set1.intersection(set2)#函数模式
print(setintersection)
print(setintersection1)

#3.4.对称差集（除了公共部分的其他部分）
setsd=set1^set2
setsd1=set1.symmetric_difference(set2)
print(setsd)
print(setsd1)
'''4.其他'''
print(6 in set2)


