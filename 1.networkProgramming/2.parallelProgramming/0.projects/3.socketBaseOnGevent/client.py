import socket
import time
from threading import Thread
def client(i):
    sk=socket.socket()
    sk.connect(('127.0.0.1',9001))
    while True:
        sk.send("I am client {}".format(i).encode())
        msg=sk.recv(1024)
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    for i in range(2):
        Thread(target=client,args=(i,)).start()