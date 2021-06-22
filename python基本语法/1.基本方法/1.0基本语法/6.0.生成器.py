'''1.生成器生成方法'''
'''1.1生成器和列表的区别 列表：[],生成器：()，注意：这个不是tuple'''
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(L)
print(g)
'''1.2.yield生成generator方法'''
def generate_generator(n):
    for i in range(n):
        yield(i)
gen=generate_generator(10)



'''2.生成器调用方法:
注意：只能生成一次，而且一定要按顺序
'''
'''2.1.列表循环取出'''
for item in gen:
    print(item)
'''2.2.__next__()方法'''
print(g.__next__())

'''2.3.next()方法'''
print(next(g))

'''2.4.例子：斐波那契数列'''
def fibiter(n):
    pre=[1,1]
    for i in range(n):
        if i<=1:
            yield pre[i]
        else:
            pre[0],pre[1]=pre[1],pre[1]+pre[0]
            yield pre[1]
for i in fibiter(20):
    print(i)


'''3.send给迭代器传入参数
注意：要先进行一次循环或者先send一个None才能send其他东西进去（其实就是让程序走到yield那里）
作用：
1.调整生成器的工作方式
2.yield 和send机制优点像线程（其实是协程：线程的分支），函数之间的互相传递信息（这样就可以交替进行）
'''

def iteration(n):
    for i in range(n):
        text=yield n
        if text!=None:
            print(text)

it=iteration(9)
it.__next__()
print(it.send('这个是send进去的text'))


'''3.1.协程'''
def task1(n):
    for i in range(n):
        print("搬砖第%d次"%i)
        yield None
def task2(n):
    for i in range(n):
        print("听第%d次歌"%i)
        yield None
t1=task1(5)
t2=task2(5)
while True:
    try:
        t1.__next__()
        t2.__next__()
    except Exception as err:
        print(err)
        break
