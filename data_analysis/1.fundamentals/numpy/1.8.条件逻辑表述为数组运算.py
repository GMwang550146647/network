
import numpy as np
#1.np.where(condition,truearr,falsearr) 对应 x if condition else y
xarr=np.arange(20)
yarr=[(a>=10) for a in xarr]
result=np.where(xarr>=10,xarr*3,0)  #意思是把xarr里面大于10的数设置为arr中对应的数乘3，否则为0，可以嵌套(不改变xarr)
print(result)