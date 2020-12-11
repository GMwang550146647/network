"""
#For Linux
$ gcc -shared -Wl,-soname,adder -o fib.so -fPIC fib.c

#For Mac
$ gcc -shared -Wl,-install_name,fib.so -o adder.so -fPIC fib.c
"""
from ctypes import *
import time
if __name__ == '__main__':
    fib = CDLL('./c_pkg/fib.so').fib
    t_start = time.time()
    result = fib(35)
    duration = time.time() - t_start
    print("using {}s result: {}".format(duration, result))