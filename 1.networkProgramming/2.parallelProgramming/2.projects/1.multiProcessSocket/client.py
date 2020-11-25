import time
import socket
from multiprocessing import Process
def request(ith=1):
    sk=socket.socket()
    sk.connect(('127.0.0.1',9001))
    for i in range(30):
        sk.send(b'hello')
        msg=sk.recv(1024).decode()
        print("user{}:\t{}".format(ith,msg))
        time.sleep(0.5)
    sk.close()

def multi_request(n_requests):
    p_list=[]
    for i in range(n_requests):
        p=Process(target=request,args=(i+1,))
        p_list.append(p)
        p.start()
    [p.join() for p in p_list]

if __name__ == '__main__':
    multi_request(50)