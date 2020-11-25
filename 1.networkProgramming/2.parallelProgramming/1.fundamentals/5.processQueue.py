from multiprocessing import Queue,Process
import time
"""
Queue： 进程共享数据
"""
def func_put(q,name='put_func'):
    msg="hello"
    while True:
        q.put(msg)
        print("{}: put {}".format(name,msg))
        time.sleep(1)

def func_get(q,name='get_func'):
    while True:
        print("{}: get {}".format(name, q.get()))

if __name__ == '__main__':
    q=Queue()
    Process(target=func_put,args=(q,)).start()
    Process(target=func_get,args=(q,)).start()
