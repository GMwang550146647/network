"""
发送
"""

import socket
import os
from threading import Thread


def serve(conn):
    from_b_msg = conn.recv(1024)
    str_msg = from_b_msg.decode('utf-8')
    path = str_msg.split('\r\n')[0].split(' ')[1]
    print('path>>>', path)
    print("msg>>>>", str_msg)

    conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
    # 由于整个页面需要html、css、js、图片等一系列的文件，所以我们都需要给人家浏览器发送过去，浏览器才能有这些文件，才能很好的渲染你的页面
    # 根据不同的路径来返回响应的内容
    path = os.path.join(CURRENT_PATH, '0.data', 'html/socket_test_myServer.html' if path == '/' else path[1:])
    with open(path, 'rb') as f:
        data = f.read()
    conn.send(data)
    # 如果不关闭就会一直保持连接，网页也会一直显示加载状态
    conn.close()
    print('sended {}!'.format(path))


if __name__ == '__main__':
    CURRENT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    sk = socket.socket()
    sk.bind(('127.0.0.1', 4001))
    sk.listen()
    t_list = []
    while True:
        conn, addr = sk.accept()
        ti = Thread(target=serve, args=(conn,))
        ti.start()
        t_list.append(ti)
