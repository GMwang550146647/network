'''
捕获异常对象
'''
print("***************************************")
'''1.捕获所有异常，并查看异常名称'''
print("before err")
try:
    print(10/0)
except Exception as err:
    print("deal with err：",err)
print("after err")

'''
2.捕获特定异常：例如NameError，
注意：只会捕获第一个，第二个不理
'''
print("before err")
print("***************************************")
try:
    print(c)
    print(10/0)
except NameError as err1:
    print("deal with err：",err1)
except ZeroDivisionError as err2:
    print("deal with err:",err2)
print("after err")
print("***************************************")
'''3.有异常，但是捕获的不是该类型，会报错'''
# print("before err")
# try:
#     print(c)
# except ZeroDivisionError as err2:
#     print("deal with err:",err2)
# print("after err")
# print("***************************************")
'''4.finally：无论出现什么语句都出现'''
print("before err")
try:
    print(c)
except ZeroDivisionError as err2:
    print("deal with err:",err2)
finally:
    print("must be exec")
print("after err")
print("***************************************")