from gevent import monkey

monkey.patch_all()
import gevent
import socket
from threading import current_thread, Thread


def server(conn, i):
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print("Current thread {}  -> Server {} -> Received {}".format(current_thread().ident % 100, i, msg))
            msg = msg.upper()
            conn.send(msg.encode())
        except ConnectionResetError as err:
            break


def build_server_gevent():
    sk = socket.socket()
    sk.bind(('127.0.0.1', 9001))
    sk.listen()
    n_servers = 0
    while True:
        conn, _ = sk.accept()
        n_servers += 1
        gi = gevent.spawn(server, conn=conn, i=n_servers)


def build_server_thread():
    sk = socket.socket()
    sk.bind(('127.0.0.1', 9001))
    sk.listen()
    n_servers = 0
    while True:
        conn, _ = sk.accept()
        n_servers += 1
        ti = Thread(target=server, args=(conn, n_servers))
        ti.start()


if __name__ == '__main__':
    build_server_gevent()
    # build_server_thread()
