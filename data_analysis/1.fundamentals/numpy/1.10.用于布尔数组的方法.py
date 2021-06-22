import numpy as np
arr=np.random.randn(25).reshape(5,5)
print(arr)
bool_arr=arr>0
print(bool_arr.sum())  #true为1，false为0
print(bool_arr.any())   #有一个True就为True
print(bool_arr.all())   #有一个False就为False

