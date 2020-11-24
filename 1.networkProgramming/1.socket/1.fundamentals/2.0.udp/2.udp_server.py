import socket
sk=socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9999))
#recvfrom 的意思是把对方地址也接收了
while True:
    msg,addr=sk.recvfrom(1024)
    print("Received from {}:\t{}".format(addr,msg))
    sk.sendto(b'hello',addr)
    print("Send:{}".format('hello'))
