"""
#For Linux
$ gcc -shared -Wl,-soname,adder -o fib.so -fPIC fib.c

#For Mac
$ gcc -shared -Wl,-install_name,fib.so -o fib.so -fPIC fib.c
"""

import time
import argparse

def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("-n", "--number", type=int, default=35,
                      help="nth number of fib")
  return parser.parse_args()

if __name__ == '__main__':
    n = parse_args().number
    t_start = time.time()
    from ctypes import *
    fib = CDLL('./methods/c_pkg/fib.so').fib
    result = fib(n)
    duration = time.time() - t_start
    print("using {}ms result: {}".format(round(duration*1000,3), result))