'''--------------------- 包 ---------------------
文件夹和包的关系：
文件夹放非py文件
包放py文件（比普通文件多了个__init__.py文件）
'''

'''5.包'''
import packageAA as pa
'''5.1.只能调用该包的__init__文件下的内容'''
print(pa.c)
'''5.2.要调用其包下的其他内容可以：'''
from packageAA import a,b
print(a.a)
print(b.b)

#或者：
from packageAA.a import a
from packageAA.b import b
print(a)
print(b)

'''6.文件功能介绍：'''
'''
__pycache__是模块的缓存文件，编译一次之后就会把导入包的缓存数据丢进去，下一编译的时候就不用再导入了，只需要更改代码部分

'''


'''7.注意：
外调里可以，里调外也可以，所有的包其实都是根据项目目录为相对目录去检索内容的
'''