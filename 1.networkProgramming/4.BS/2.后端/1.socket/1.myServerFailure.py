"""
根据http协议发送请求
    socket是应用层和传输层之间的抽象层，每次都有协议，协议就是消息格式，那么传输层的消息格式我们不用管，因为socket帮我们搞定了，但是应用层的
    协议还是需要咱们自己遵守的，所以再给浏览器发送消息的时候，如果没有按照应用层的消息格式来写，那么你返回给浏览器的信息，浏览器是没法识别的。
    而应用层的协议就是我们的HTTP协议，所以我们按照HTTP协议规定的消息格式来给浏览器返回消息就没有问题了，关于HTTP我们会细说，首先看一下直接写
    conn.send(b'hello')的效果，然后运行代码，通过浏览器来访问一下，然后再看这一句conn.send(b'HTTP/1.1 200 ok \r\n\r\nhello')的效果
"""

import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 4000))
sk.listen()
while True:
    # 1.请求-响应 模式
    conn, addr = sk.accept()
    from_b_msg = conn.recv(1024)
    str_msg = from_b_msg.decode('utf-8')
    print(str_msg)

    # 下面这句就是按照http协议来写的
    conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
    with open('../0.data/html/socket_test_myServer.html', 'r') as f:
        content = f.read().encode()
    conn.send(content)
    # 2.无连接，无状态保存
    conn.close()
    # 注意：上面每一个请求处理完之后，都有一个conn.close()是因为，HTTP协议是短链接的，一次请求对应一次响应，这个请求就结束了，
    # 所以我们需要写上close，不然浏览器自己断了，你自己写的服务端没有断，就会出问题。
