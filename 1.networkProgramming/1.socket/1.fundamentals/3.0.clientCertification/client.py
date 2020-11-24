import socket
import hashlib
import os
from protocal import confirm_func_hash,confirm_func_hmac

SECRET_KEY=b'alex_sb'
#1.建立连接
sk=socket.socket()
sk.connect(("127.0.0.1",9002))
#2.获取随机数字，通过一套相同的处理方式得出答案
rand_msg=sk.recv(32)
res=confirm_func_hmac(rand_msg,SECRET_KEY)
#3.返回答案
sk.send(res)
#4.接收服务器的验证结果
msg=sk.recv(1024)
print(msg)
if msg:
    print("connected")
else:
    print("not connected")