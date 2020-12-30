"""
发送
"""

import socket
import os

CURRENT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sk = socket.socket()
sk.bind(('127.0.0.1', 4099))
sk.listen()

while True:
    try:
        conn, addr = sk.accept()
        from_b_msg = conn.recv(1024)
        str_msg = from_b_msg.decode('utf-8')
        path = str_msg.split('\r\n')[0].split(' ')[1]
        print('path>>>', path)
        print("msg>>>>", str_msg)

        conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
        # 由于整个页面需要html、css、js、图片等一系列的文件，所以我们都需要给人家浏览器发送过去，浏览器才能有这些文件，才能很好的渲染你的页面
        # 根据不同的路径来返回响应的内容
        path=os.path.join('1.信息收集卡.html' if path=='/' else path[1:])
        with open(path, 'rb') as f:
            data = f.read()
        conn.send(data)
        conn.close()
        print('sended {}!'.format(path))
    except Exception as err:
        print(err)