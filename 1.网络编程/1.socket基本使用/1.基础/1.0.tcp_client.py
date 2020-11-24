import socket


sk = socket.socket()
#1.建立连接
sk.connect(("127.0.0.1", 1998))
while True:
    #2.发送与接收
    msg = sk.recv(1024)
    print("received:{}".format(msg))
    send_msg=input('Please input msg:').encode('utf-8')
    sk.send(send_msg)
    if send_msg == b'exit':
        break
sk.close()


