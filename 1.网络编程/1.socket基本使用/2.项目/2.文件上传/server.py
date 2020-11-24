import socket
import os
from utility.protocal import download_file

if __name__ == '__main__':
    SAVE_DIR='serverfile'
    server_port=("127.0.0.1", 9002)
    sk = socket.socket()
    sk.bind(server_port)
    sk.listen()
    while True:
        conn,addr=sk.accept()
        download_file(conn,SAVE_DIR)
        conn.close()
    sk.close()
