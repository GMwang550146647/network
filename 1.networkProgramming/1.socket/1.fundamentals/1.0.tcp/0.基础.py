"""
tcp:
    socket() 创建tcp套接字
    bind()   绑定端口
    listen() 监听
    accept() 等待client的到访
    send()   发送消息，不需要地址
    recv()   只接受消息
    connect  客户端/tcp协议方法，和server建立连接
    close    关闭服务/连接

udp:
    socket(type=socket.SOCK_DGRAM)
    sendto() 需要地址
    recvfrom 接收消息和地址

"""