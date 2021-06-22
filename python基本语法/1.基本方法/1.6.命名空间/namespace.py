'''
命名空间：
'''
'''1.获取当前命名空间'''
a=100
scope=locals()
print(scope)
print(scope['a'])

'''2.获取全局命名空间'''

global_scope=globals()
print(global_scope)