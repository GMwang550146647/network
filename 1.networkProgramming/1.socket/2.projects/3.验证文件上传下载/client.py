import socket
import os
import logging
import json
from utility.protocal import DataApi



class Client():
    def __init__(self, name="gm"):
        self.name = name
        self._SECRET_KEY = b"GMWANG"
        self.da = DataApi()
        self.logger = logging.Logger(__file__)
        self.DATA_DIR = "data/client"

    def connect(self, server_port):
        sk = socket.socket()
        sk.connect(server_port)
        return sk

    def user_verify(self, conn):
        try:
            rand = conn.recv(32)
            res = self.da.confirm_func_hmac(rand, self._SECRET_KEY)
            conn.send(res)
            msg=conn.recv(1024)
            success=True if msg else False
            if success:
                self.logger.info("Receive Response:{}".format(res))
            return success
        except Exception as err:
            return False

    def upload_download_request(self,conn):
        finish=False
        while not finish:
            task = input("Upload or Download?\n>>>").lower()
            if task=='upload':
                self.da.tcp_send(task,conn)
                files=self.da.scan_files(self.DATA_DIR)
                filei=input("Which file do you want to upload?\n{}\n>>>".format("\t".join(list(files.keys()))))
                if filei in files:
                    self.da.upload_file(files[filei],conn)
                    self.logger.info("Successfully uploaded {}".format(filei))
                else:
                    self.logger.error("File not found")
            elif task=='download':
                self.da.tcp_send(task, conn)
                files=json.loads(self.da.tcp_receive(conn))
                filei = input("Which file do you want to download?\n{}\n>>>".format("\t".join(list(files.keys()))))
                if filei in files:
                    self.da.tcp_send(filei,conn)
                    exist=self.da.tcp_receive(conn)
                    if exist=='ok':
                        download_file=self.da.download_file(self.DATA_DIR, conn)
                        self.logger.info("Successfully downloaded {}".format(download_file))
                    else:
                        self.logger.error("Server Error,file not found")
                else:
                    self.logger.error("File not found")
            else:
                self.logger.error("Incapable of Action ")
            flag = input("Continue? y or n ?\n>>>").lower()
            finish= False if flag=='y' else True

    def handle(self, server_port):
        conn = self.connect(server_port)
        if self.user_verify(conn):
            self.logger.info("Connection Success!")
            self.upload_download_request(conn)

        else:
            self.logger.error("Connection Failure!")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    server_port = ("127.0.0.1", 9900)
    Client().handle(server_port)
