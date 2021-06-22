'''
自定义异常并抛出
'''
'''1.抛出异常'''
def add(a,b):
    if a<0 or b<0:
        raise Exception
    sum=a+b
    return sum
try:
    add(10,-2)
except Exception as err:
    print(err)

'''2.抛出自定义异常'''
class myError(Exception):
    def __str__(self):
        return '错误了，傻老'
def add(a,b):
    if a<0 or b<0:
        raise myError
    sum=a+b
    return sum
try:
    add(10,-2)
except  Exception as err:
    print(err)