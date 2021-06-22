'''
异常出现的地方：
api:built-in exceptions
'''
'''
1.如果函数内处理异常，就不会传到函数外
'''
def fn():
    print("hello fn")
    try:
        print(10/0)
    except Exception as err:
        print(err)

fn()

'''
2.如果函数内没处理异常，应在函数外处理
'''
def fn1():
    print("hello fn1")
    print(10/0)
try:
    fn1()
except Exception as err:
    print(err)

'''
3.如果没有处理，向调用出传播，直至全局作用域，如果依然没处理，程序终止，显示异常信息
出现异常会保存到一个专门的异常对象中，然后传到上一层调用处
'''
def func():
    print("func")
    return 10/0
def func1():
    print("func1")
    func()
def func2():
    print("func2")
    func1()
def func3():
    print("func3")
    func2()
