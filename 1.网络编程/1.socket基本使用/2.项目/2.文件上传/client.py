import socket
import os
from utility.protocal import upload_file


if __name__ == '__main__':
    INPUT_DIR = 'clientfile'
    file = os.path.join(INPUT_DIR, 'python.pdf')
    server_port = ("127.0.0.1", 9002)
    sk=socket.socket()
    sk.connect(server_port)
    upload_file(file,sk)
    sk.close()
