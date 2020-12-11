
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
    result=fib(35)
    duration=time.time()-t_start
    print("using {}s result: {}".format(duration,result))