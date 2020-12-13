import sys
import gc
import sys


def test_counter():
    class Test():
        def __init__(self):
            pass

    recur_t = Test()
    k = recur_t
    recur_t._self = recur_t
    # 由于进入sys.getrefcount函数的时候，形参传递都会对数据进行引用，把该引用减去（-1）就好
    # sys.getrefcount函数用来查看一个对象有几个引用print sys.getrefcount(k)####结果####32
    print("recur_t count: ",sys.getrefcount(recur_t) - 1)
    print("k count:", sys.getrefcount(k) - 1)
    del k
    print("After del k recur_t count: ",sys.getrefcount(recur_t) - 1)
    del recur_t
    print(gc.collect())

if __name__ == '__main__':
    test_counter()
