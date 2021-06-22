'''
异常处理：
异常不是为了终止程序，而是对异常进行处理
'''
'''1.基本格式'''
"""
try 语句：
    有可能出错的代码
except:
    出错了怎么处理的代码
else:
    没错的话执行这个
"""
try:
    10/0
    print("try 完了")
except Exception as err:
    print("出错了，哈哈哈:",err)
else:
    print("没错，哈哈哈")