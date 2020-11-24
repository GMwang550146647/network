import logging
import struct
import json
import os
import hashlib
import hmac
ENCRYPT="utf-8"
BUFFER_SIZE=1024
class DataApi():
    def __init__(self):
        pass

    def scan_files(self,dir):
        return {filei: os.path.join(dir,filei) for filei in os.listdir(dir)}

    def tcp_receive(self,connection):
        #注意 struct.pack()函数一定是压缩成4字节
        msg_len=struct.unpack('i',connection.recv(4))
        msg=connection.recv(msg_len[0]).decode(ENCRYPT)
        logging.info("Received:\t{}\t{}".format(msg_len,msg))
        return msg

    def tcp_send(self,msg,connection):
        u_msg = msg.encode(ENCRYPT)
        u_str_len = struct.pack('i',len(u_msg))
        connection.send(u_str_len)
        connection.send(u_msg)
        logging.info("Sended:\t{}\t{}".format(u_str_len,msg))

    def upload_file(self,file,conn):
        file_size=os.path.getsize(file)
        msg_header = {"file_name": os.path.basename(file), "file_size": file_size}
        msg_header=json.dumps(msg_header)
        self.tcp_send(msg_header,conn)
        with open(file,'rb') as f:
            while file_size>0:
                content=f.read(BUFFER_SIZE)
                file_size-=BUFFER_SIZE
                conn.send(content)

    def download_file(self,file_dir,conn):
        msg_header = json.loads(self.tcp_receive(conn))
        with open(os.path.join(file_dir,msg_header['file_name']),'wb') as f:
            while msg_header['file_size']>0:
                content=conn.recv(BUFFER_SIZE)
                msg_header['file_size']-=len(content)
                f.write(content)
        return msg_header['file_name']

    def confirm_func_hash(self,rand,secret_key):
        sha = hashlib.sha1(secret_key)
        sha.update(rand)
        res = sha.hexdigest()
        res=res.encode()
        return res

    def confirm_func_hmac(self,rand,secret_key):
        h=hmac.new(secret_key,rand)
        res=h.digest()
        return res