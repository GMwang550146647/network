import socket
sk=socket.socket(type=socket.SOCK_DGRAM)
sk.bind(("127.0.0.1",9000))
while True:
    msg,addr=sk.recvfrom(1500)
    print("Client:\t{}".format(msg.decode()))
    content=input("Server:\t")
    sk.sendto(content.encode(),addr)
    if content.upper()=="Q":break
