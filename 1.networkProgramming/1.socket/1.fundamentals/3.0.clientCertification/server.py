import socket
import os
import hashlib
from protocal import confirm_func_hash,confirm_func_hmac
#1.建立服务器
SECRET_KEY=b'alex_sb'
sk=socket.socket()
sk.bind(("127.0.0.1",9002))
sk.listen()
while True:
    try:
        #2.等待连接
        conn,addr=sk.accept()
        #3.接收到连接，首先要验证：发送随机字段，让client和server执行同一个映射函数
        rand_msg=os.urandom(32)
        conn.send(rand_msg)
        res=confirm_func_hmac(rand_msg,SECRET_KEY)
        res_client=conn.recv(1024)
        print("server:{}".format(res))
        print("clent:{}".format(res_client))
        #4.如果结果不一样，切断连接
        if res_client==res:
            print("Leagel")
            conn.send(b"hello")
        else:
            conn.close()
    except Exception as err:
        break
sk.close()