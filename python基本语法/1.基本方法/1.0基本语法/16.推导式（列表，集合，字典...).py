'''1.列表推导式'''
'''1.1.循环推导式'''
arr=[1,2,3,4,5,6,7,8,9]
arr11=[i**2 for i in arr]
print(arr11)


'''1.2.if-else'''
arr121=[i**2  for i in arr if i%2==0]   #不带else的时候在后面放
print(arr121)
arr122=[i**2  if i%2==0 else i**4 for i in arr] #带else的时候在前面放
print(arr122)

'''2.集合推导式'''
'''2.1.循环推导式'''
arr21={x+1 for x in arr if x%2==0}
print(arr21)

'''3.字典推导式'''
#key 和value交换
dict1={'a':1,'b':2,'c':4,'d':4}   #注意，这里有两个4，会出现重复的现象
# dict2={dict1[a]:a for a in dict1}  #或者这个
dict2={value:key for key,value in dict1.items()}
print(dict2)