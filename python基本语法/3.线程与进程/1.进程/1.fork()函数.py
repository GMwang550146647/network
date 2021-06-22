'''
1.fork()函数
子进程：返回0
父进程：返回子进程的pid
'''
import os
print('Process(%s) start...'%os.getpid())
pid=os.fork()
if pid==0:
    '''子进程要做的事情'''
    print("I am child process(%s) and my parent is %s"%(os.getpid(),os.getppid()))
else:
    '''父进程要做的事情'''
    print("I (%s) just created a child process (%s)."%(os.getpid(),pid))
