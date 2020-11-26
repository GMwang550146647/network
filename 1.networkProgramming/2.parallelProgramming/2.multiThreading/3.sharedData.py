from threading import  Thread
import time
n=1000

def func():
    global n
    n-=1
    time.sleep(0.1)
    n-=1

if __name__ == '__main__':
    t_list=[]
    for i in range(1000):
        t=Thread(target=func)
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()
    print(n)