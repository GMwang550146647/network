import numpy as np
#1.维度
arr=np.array([[1,2,3],[4,5,6]])
print(arr.shape)
#2.数据类型
print(arr.dtype)
#默认np.xxx
# int8 uint8               有、无符号整形（1字节）8位  -128到127   0到255
# int16 uint16
# int32 uint32
# int64（默认） uint64
# float16
# float32
# float64(默认）
# float128
#3.数据类型转换
arr_as=arr.astype(np.float32)
print(arr_as.dtype)
#或者创建的时候加上
arr_as=np.array([[1,2,3],[4,5,6]],dtype=np.int32)