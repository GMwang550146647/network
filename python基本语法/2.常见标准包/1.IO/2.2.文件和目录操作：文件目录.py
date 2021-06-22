import os
# 创建一个目录:
os.mkdir('/Users/michael/testdir') #要求前面的目录已创建
os.mkdirs('/Users/michael/testdir',exist_ok=True) #中间的目录如果不存在则创建，如果目录已存在，则会报错（若exist_ok=False)
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')
# 获取当前目录结构
os.listdir('/')
# 对文件重命名:
os.rename('test.txt', 'test.py')
# 删掉文件:
os.remove('test.py')