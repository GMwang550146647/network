
import socket
sk=socket.socket(type=socket.SOCK_DGRAM)
server=('127.0.0.1',9999)
while True:
    send_msg=input("Please input send_msg:")
    sk.sendto(send_msg.encode("utf-8"),server)
    reveive_msg=sk.recv(1024)
    print("Sended:{}".format(reveive_msg))