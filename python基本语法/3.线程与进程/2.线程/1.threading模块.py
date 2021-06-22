import time, threading
'''
1.由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，
它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。
名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
'''
# 新线程执行的代码:


'''1.1.子线程跑的程序'''
def loop(n=5):
    print('thread %s is running...' % threading.current_thread().name)
    for i in range(n):
        print('thread %s >>> %s' % (threading.current_thread().name, i))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


'''1.2.多线程主程序一般格式'''
print('thread %s is running...' % threading.current_thread().name)
t=[]
for i in range(10):
    ti = threading.Thread(target=loop, name='LoopThread%s'%i,args=(i,)) #args是该程序需要的参数，要几个写几个
    t.append(ti)
for i in range(10):
    t[i].start()  #线程开始
for i in range(10):
    t[i].join()   #主线程等待其他线程结束
print('thread %s ended.' % threading.current_thread().name)