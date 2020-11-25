import socket
from multiprocessing import Process


def handle(conn):
    while True:
        try:
            print("Client:{}".format(conn))
            msg = conn.recv(1024).decode()
            ret = msg.upper().encode()
            conn.send(ret)
        except ConnectionResetError:
            break
    conn.close()


def build_server(addr):
    sk = socket.socket()
    sk.bind(addr)
    sk.listen()
    while True:
        try:
            conn, addr = sk.accept()
            Process(target=handle, args=(conn,)).start()
        except ConnectionResetError:
            break
    print("All Done")


if __name__ == '__main__':
    addr = ('127.0.0.1', 9001)
    build_server(addr=addr)
