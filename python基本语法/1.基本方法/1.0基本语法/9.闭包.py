'''
闭包：
1.函数中定义的函数
2.外部函数把内部函数返回
3.这内部函数引用外部函数的值


作用：
1.保存并返回闭包时的状态（外层函数变量）

实现原理：
由于函数还没去除引用，所以其对应的内存尚未被消掉
'''

'''1.调用外层函数的值'''
def outterfunc(c):
    a=100
    def inner_func():
        b=99
        print(a,b,c)
    print(locals())
    return inner_func

x=outterfunc(10)
x()

'''2.调用同级函数'''

def outfun(c):
    a=100
    def innerfun1():
        print(a,c)
    def innerfun2():
        print("innerfunc2:")
        innerfun1()
    return innerfun2

func=outfun(1000)
func()

'''3.闭包应用：计数器'''
def generateCounter():
    counter=[0]
    def add_one():
        counter[0]+=1
        print('第%d次访问'%counter[0])
    return add_one
counter=generateCounter()
for i in range(5):
    counter()