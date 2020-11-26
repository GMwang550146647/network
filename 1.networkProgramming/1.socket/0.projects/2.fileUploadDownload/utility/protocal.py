import logging
import struct
import json
import os

ENCRYPT="utf-8"
BUFFER_SIZE=1024

def tcp_receive(connection):
    #注意 struct.pack()函数一定是压缩成4字节
    msg_len=struct.unpack('i',connection.recv(4))
    msg=connection.recv(msg_len[0]).decode(ENCRYPT)
    logging.info("Received:\t{}\t{}".format(msg_len,msg))
    return msg

def tcp_send(msg,connection):
    u_msg = msg.encode(ENCRYPT)
    u_str_len = struct.pack('i',len(u_msg))
    connection.send(u_str_len)
    connection.send(u_msg)
    logging.info("Sended:\t{}\t{}".format(u_str_len,msg))

def upload_file(file,conn):
    file_size=os.path.getsize(file)
    msg_header = {"file_name": os.path.basename(file), "file_size": file_size}
    msg_header=json.dumps(msg_header)
    tcp_send(msg_header,conn)
    with open(file,'rb') as f:
        while file_size>0:
            content=f.read(BUFFER_SIZE)
            file_size-=BUFFER_SIZE
            conn.send(content)

def download_file(conn,file_dir):
    msg_header = json.loads(tcp_receive(conn))
    with open(os.path.join(file_dir,msg_header['file_name']),'wb') as f:
        while msg_header['file_size']>0:
            content=conn.recv(BUFFER_SIZE)
            msg_header['file_size']-=len(content)
            f.write(content)

