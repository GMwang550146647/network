import threading,time

def run1(n):
    """
    这样的写法有风险
    """
    semaphore.acquire()   #获取信号量
    time.sleep(1)   #每隔1秒弹出一次运行结果
    print("run the thread: %s"%n)
    semaphore.release()    #释放信号量

def run(n):
    with semaphore:
        time.sleep(1)  # 每隔1秒弹出一次运行结果
        print("run the thread: %s" % n)

if __name__=='__main__':
    semaphore=threading.BoundedSemaphore(6)   #声明semaphore实例，每次允许6个线程同时运行
    t_list=[]
    for i in range(30):     #循环30个线程
        t=threading.Thread(target=run,args=(i,))  #定义线程
        t.start()  #启动线程
        t_list.append(t)
    [t.join() for t in t_list]