import threading
import time
class ThreadSort():
    def __init__(self,arr):
        self.arr=arr
        self.sorted_arr=[]
    def sleep_print(self,sec):
        time.sleep(sec/10000.0)
        # print(sec)
        self.sorted_arr.append(sec)

    def thread_sort(self):
        n_threads=len(self.arr)
        threads = []
        for i in range(n_threads):
            t = threading.Thread(target=self.sleep_print, args=((self.arr[i],)))
            threads.append(t)
        # run
        for i in range(n_threads):
            threads[i].setDaemon(True)
            threads[i].start()
        # wait
        for i in range(n_threads):
            threads[i].join()
        print(self.sorted_arr)
if __name__=='__main__':
    arr=sorted(list(range(1000)),reverse=True)
    t=time.time()
    ThreadSort(arr).thread_sort()
    print('thread_sort:',time.time()-t)
    t=time.time()
    sorted(arr)
    print('quick_sort:',time.time()-t)
