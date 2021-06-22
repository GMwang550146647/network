import os
print(os.name) #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.uname())#注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
'''1.环境变量'''
#1.1.环境变量：
print(os.environ)
#1.2.获取任一环境变量值
print(os.getenv('PATH'))

'''2.文件目录'''
# 查看当前目录的绝对路径:
# 在某个目录下创建一个新目录，
# 2.1.首先把新目录的完整路径表示出来:
print(os.path.abspath('.'))  #绝对路径（可能是软连接）
print(os.path.realpath('.')) #标准路径，非软连接路径
# '/Users/michael'
# 2.2.把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# part-1/part-2
# 而Windows下会返回这样的字符串：
# part-1\part-2
print(os.path.join('/Users/michael', 'testdir'))
# '/Users/michael/testdir'
#2.3.拆分路径
print(os.path.split('/Users/michael/testdir/file.txt'))
# ('/Users/michael/testdir', 'file.txt')

#2.4.获取指定文件所在文件目录
print(os.path.dirname('/Users/michael/testdir/file.txt'))
print(os.path.dirname(os.path.dirname('/Users/michael/testdir/file.txt'))) #嵌套多一层就是前一个的文件夹

'''3.判断是否'''
#是否绝对路径
print(os.path.isabs('.'))
#是否文件
print(os.path.isfile('.'))
#是否文件夹
print(os.path.isdir('.'))