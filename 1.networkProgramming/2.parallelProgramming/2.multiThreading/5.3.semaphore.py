import threading,time
class Run():
    def __init__(self):
        self.semaphore=threading.BoundedSemaphore(6)  # 声明semaphore实例，每次允许6个线程同时运行
    def func_unsafe(self,n):
        """
        这样的写法有风险
        """
        self.semaphore.acquire()   #获取信号量
        time.sleep(0.01)   #每隔1秒弹出一次运行结果
        print("run the thread: %s"%n)
        self.semaphore.release()    #释放信号量

    def func_safe(self,n):
        with self.semaphore:
            time.sleep(0.01)  # 每隔1秒弹出一次运行结果
            print("run the thread: %s" % n)
    def run(self,safe_mode=True,n_threads=300):
        t_list = []
        for i in range(n_threads):  # 循环30个线程
            t = threading.Thread(target=self.func_safe if safe_mode else self.func_unsafe, args=(i,))  # 定义线程
            t.start()  # 启动线程
            t_list.append(t)
        [t.join() for t in t_list]

if __name__=='__main__':
    Run().run(safe_mode=True)
    Run().run(safe_mode=False)