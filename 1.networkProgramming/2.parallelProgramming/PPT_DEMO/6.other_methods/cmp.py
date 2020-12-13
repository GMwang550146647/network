"""
python test3.py
pypy test3.py
python fib_use_C.py
"""
import subprocess

if __name__ == '__main__':
    # 1. 比较
    cmd1 = "python methods/fib.py".split()
    cmd2 = "pypy methods/fib.py".split()
    cmd3 = "python methods/fib_useC.py".split()
    print(cmd1)
    subprocess.call(cmd1)
    print(cmd2)
    subprocess.call(cmd2)
    print(cmd3)
    subprocess.call(cmd3)

    # 2. 编译并执行C
    file_name = 'fib'
    cmd41 = "gcc -o methods/c_pkg/{} methods/c_pkg/fib.c".format(file_name).split()
    cmd42 = "methods/c_pkg/{}".format(file_name).split()
    subprocess.call(cmd41)
    subprocess.call(cmd42)
