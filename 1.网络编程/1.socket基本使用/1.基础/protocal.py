import logging
import struct

ENCRYPT="utf-8"
def tcp_receive(connection):
    #注意 struct.pack()函数一定是压缩成4字节
    msg_len=struct.unpack('i',connection.recv(4))
    msg=connection.recv(msg_len[0]).decode(ENCRYPT)
    logging.info("Received:\t{}".format(msg))
    return msg

def tcp_send(msg,connection):
    u_msg = msg.encode(ENCRYPT)
    u_str_len = struct.pack('i',len(u_msg))
    connection.send(u_str_len)
    connection.send(u_msg)
    logging.info("Sended:\t{}".format(msg))