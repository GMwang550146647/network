import numpy as np
arr=np.arange(10)
#1.二进制格式存取
#保存
np.save('1.13.array',arr)
#获取
arr_load=np.load('1.13.array.npy')
#2.存取文本文件
arr=np.savetxt('array_ex.txt',arr_load)
arr=np.loadtxt('array_ex.txt',delimiter=',')
