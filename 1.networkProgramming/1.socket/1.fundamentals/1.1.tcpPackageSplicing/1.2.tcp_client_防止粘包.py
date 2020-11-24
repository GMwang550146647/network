import socket
from protocal import tcp_receive,tcp_send

data=['hello']*1000+["exit"]
sk = socket.socket()
sk.connect(("127.0.0.1", 10000))
for datai in data:
    tcp_send(datai,sk)
sk.close()