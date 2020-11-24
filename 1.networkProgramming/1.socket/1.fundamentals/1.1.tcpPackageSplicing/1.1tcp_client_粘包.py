import socket


sk = socket.socket()
sk.connect(("127.0.0.1", 10000))
while True:
    msg = sk.recv(1024)
    print("received:{}".format(msg))
    send_msg=input('Please input msg:').encode('utf-8')
    sk.send(send_msg)
    sk.send("Second msg".encode('utf-8'))
    if send_msg == b'exit':
        break
sk.close()


