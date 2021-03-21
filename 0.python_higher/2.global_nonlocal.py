gcount = 0
"""
一.global
"""


def global_test1():
    '''
    1.global关键字用来在函数或其他局部作用域中使用全局变量。(修改的时候要声明)
    '''
    global gcount
    gcount += 1
    print(gcount)


def global_test2():
    '''
    2.但是如果不修改全局变量也可以不使用global关键字
    '''
    print(gcount)


'''
二.nonlocal
'''


def make_counter():
    gcount = 0

    def counter():
        nonlocal gcount
        gcount += 1
        return gcount

    return counter


def nonlocal_test():
    mc = make_counter()
    print(mc())
    print(mc())
    print(mc())


'''
三.如果外层已存在，声明nonlocal和global会采用外层的变量
    如果不存在，声明nonlocal和global会把变量加入到外层的变量空间中
'''


def scope_test():
    '''
    3.
    '''

    def do_local():
        spam = "local spam"  # 此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错

    def do_nonlocal():
        nonlocal spam  # 使用外层的spam变量
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignmane:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


if __name__ == '__main__':
    global_test1()
    global_test2()
    nonlocal_test()
    scope_test()
    print("In global scope:", spam)
