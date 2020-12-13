
"""
pypy -m pip install xxx
"""

def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1) +fib(n-2)
import time
if __name__ == '__main__':
    t_start=time.time()
    result=fib(30)
    duration=time.time()-t_start
    print("using {}ms result: {}".format(round(duration*1000,3),result))