import dis

a = 0
p = []


def func1():
    global a
    a += 1


def func2():
    global p
    p.append(1)


"""
dis.dis()->查看机器指令
所有的机器操作详情如下：
1. += -=

  5           0 LOAD_GLOBAL              0 (a)
              2 LOAD_CONST               1 (1)
->非原子操作    4 INPLACE_ADD
->非原子操作   6 STORE_GLOBAL             0 (a)
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
2. append pop 
  9           0 LOAD_GLOBAL              0 (p)
              2 LOAD_METHOD              1 (append)
              4 LOAD_CONST               1 (1)
->原子操作     6 CALL_METHOD              1
             8 POP_TOP
             10 LOAD_CONST               0 (None)
             12 RETURN_VALUE
"""
if __name__ == '__main__':
    dis.dis(func1)
    print("________________THIS IS A SEPARATION LINE________________")
    dis.dis(func2)