import socket
import os
import socketserver
import time
import logging
import json
from utility.protocal import DataApi
"""
多线程访问的tcp server
"""


class MyServer(socketserver.BaseRequestHandler):

    def upload_download_service(self,conn):
        while True:
            task=self.da.tcp_receive(conn).lower()
            if task=='upload':
                download_file=self.da.download_file(self.DATA_DIR,conn)
                self.logger.info("Successfully receive upload file: {}".format(download_file))
            elif task=='download':
                files=self.da.scan_files(self.DATA_DIR)
                self.da.tcp_send(json.dumps(files),conn)
                target_file=self.da.tcp_receive(conn)
                if target_file in files:
                    self.da.tcp_send("ok",conn)
                    self.da.upload_file(files[target_file],conn)
                else:
                    self.logger.error("File not found")
            else:
                break


    def user_verify(self, conn):
        rand = os.urandom(32)
        conn.send(rand)
        res = self.da.confirm_func_hmac(rand, self._SECRET_KEY)
        res_client = conn.recv(1024)
        # 如果结果不一样，切断连接
        if res_client == res:
            self.da.tcp_send("User Verified! Begin to Communicate",conn)
            return True
        else:
            conn.close()
            return False

    def handle(self):
        self.da = DataApi()
        self._SECRET_KEY = b"GMWANG"
        self.DATA_DIR = "data/server"
        self.logger = logging.Logger(__file__)
        conn = self.request
        if self.user_verify(conn):
            try:
                self.upload_download_service(conn)
            except Exception as err:
                self.logger.error(err)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9900), MyServer)
    server.serve_forever()
