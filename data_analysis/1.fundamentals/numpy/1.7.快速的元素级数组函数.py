import numpy as np
arr=np.arange(10)
#####################一元函数#################
#1.幂函数
#1.1sqrt 开方 相当于x**0.5
arr_sqrt=np.sqrt(arr)
print(arr_sqrt)
#1.2.square 相当于 x**2
#2.exp 指数函数
arr_exp=np.exp(arr)
print(arr_exp)
#3.log
arr_log=np.log(arr)
arr_log10=np.log10(arr)
arr_log2=np.log2(arr)
arr_log1p=np.log1p(arr) #log(1+x)
#4.取整函数
#4.1.sign 正数:1,零：0，负数：-1
#4.2.ceil(大于等于该数的最小整数）
#4.3.floor(小于等于该数的最小整数）
#4.4.rint(四舍五入）
#4.5.modf(小数和整数部分以两个独立数组返回）(小数在前，整数在后）
arr_tempt=arr/2.0
arr_modf=np.modf(arr_tempt)
print(arr_modf)

#5.三角函数
#5.1.三角函数cos,cosh,sin,sinh,tan,tanh
#5.2.反三角函数：arccos, arccosh,arc.......

#6.判断无穷和有穷
#6.1.isfinite
#6.2.isinf

####################二元函数#################
#1.加减乘除
#add,subtract,mulplt,divide(floor_divide丢掉余数)
#2.power
#3.maximum minimum
#4.mod
#5.copysign(第二个数组中的符号赋给第一个数组的值）
#6.&与，|或，^非
#7.>,>=,...