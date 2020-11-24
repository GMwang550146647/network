import socket
sk=socket.socket(type=socket.SOCK_DGRAM)
while True:
    content=input("Me:\t").encode()
    sk.sendto(content,("127.0.0.1",9000))
    msg=sk.recv(1024).decode()
    print("Server:\t{}".format(msg))