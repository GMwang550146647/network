"""random模块"""

import random

'''1.random.random()'''
ran=random.random() #0-1的随机小数
print(ran)

'''2.random.randrange()'''
ran=random.randrange(1,10,2) #相当于range函数，不过是随机选一个
print(ran)

'''3.random.randint()'''
ran=random.randint(1,10)   #包括最后一个
print(ran)

'''4.random.choice()'''
ran=random.choice([1,2,3,4,5,6,9]) #列表中随机选择一个
print(ran)
ran=random.choices([1,2,3,4,5,6,9],k=2) #列表中随机选择k个
print(ran)

'''5.random.shuffle()'''
arr=[1,2,3,4,5]
ran=random.shuffle(arr)   #洗牌打乱列表顺序,return None
print(arr)

