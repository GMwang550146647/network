import socketserver
import time
"""
多线程访问的tcp server
"""
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn=self.request
        while True:
            try:
                content=conn.recv(1024).decode()
                conn.send(content.upper().encode())
                time.sleep(1)
            except ConnectionResetError:
                break

if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',9001),MyServer)
    server.serve_forever()
