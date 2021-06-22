import numpy as np
#1.sort函数默认从小到大排序，并改变原数组
arr=np.random.randn(16).reshape(4,4)
arr.sort(0)
print(arr)