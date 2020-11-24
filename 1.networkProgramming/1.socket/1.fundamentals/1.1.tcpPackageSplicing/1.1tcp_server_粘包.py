import socket

sk=socket.socket()
#1.绑定地址
#sk:向操作系统申请的资源
sk.bind(('127.0.0.1',10000))
#2.监听
sk.listen()
#3.与多个客户端进行交流
while True:
    #4.与多个客户端建立连接（握手）
    conn,addr=sk.accept()
    #5.数据交流
    while True:
        conn.send(b'hello')
        response=conn.recv(1024)
        print("reveived:{}".format(response.decode('utf-8')))
        if response==b'exit':
            break
    #6.切断连接（挥手）
    conn.close()

sk.close()