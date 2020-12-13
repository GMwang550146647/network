
"""
pypy -m pip install xxx
"""
import argparse

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("-n", "--number", type=int,default=35,
                      help="nth number of fib")
  return parser.parse_args()
def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1) +fib(n-2)
import time
if __name__ == '__main__':
    n=parse_args().number
    t_start=time.time()
    result=fib(n)
    duration=time.time()-t_start
    print("using {}ms result: {}".format(round(duration*1000,3),result))