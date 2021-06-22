'''
注意：项目>包>模块>类>函数>变量
1.模块：把功能相近的函数和类放在同一个文件夹里面
2.操作：import 模块名字就能导入模块里面的所有内容
3.作用：1.解决同名冲突问题
4.简介：
        标准库：
        builtins   系统自动导入的，其他需要自己导入
        math
        random
        time
        datatime
        calendar
        hashlib
        copy
        functools
        os
        re
        sys
        multiprocessing
        threading
        json
        logging...
'''
'''1.方法一：import module'''
import module
print(module.gm)
'''2.方法二：import module as m
注意：import两次，但是只执行一次
'''
import module as m
print(m.gm)

'''3.方法三：指定引入某些变量'''
# from module import gm
# from module import func
# from module import gm,func
from module import * #引入全部
# from module import func as f  #引入再起别名

'''4.import 限制'''
'''4.1.只能在模块内使用的变量或者函数前面加个"_"例如 "_gm"'''
# print(_gm1) #报错，不能执行
# _hiddenFunc() #报错，不能执行
func("gmwang")
'''使用该模块的内容'''
m.func(m.gm)
a=m.A("gmwang",19)
print(a)
'''4.2.__all__限制'''
#只能获取mudule的__all__规定的元素
# print(m.gmnotinall) #这个变量就会报错



