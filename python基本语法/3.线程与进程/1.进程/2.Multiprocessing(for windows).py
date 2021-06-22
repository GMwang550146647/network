
'''
2.Multiprocessing：
      由于windows没有fork调用，所以特别提供跨平台的多进程模块'''
from multiprocessing import Process
import os
def run_proc(name):
    print("Run child process%s(%s)..."%(name,os.getpid()))

print('Parent process %s.' % os.getpid())
p = Process(target=run_proc, args=('test',))
print('Child process will start.')
p.start()
p.join() #join(等待子进程结束后再往下执行）
print('Child process end.')
