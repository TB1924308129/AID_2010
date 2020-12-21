from select import select
from socket import *
import re


class Analysis:
    def __init__(self, connfd):
        self.sock = connfd

    def analysis(self, data):
        pattern = r"[A-Z]+\s+(/\S*)"
        result = re.match(pattern, data)
        if result:
            info = result.group("info")
            print(info)
        return


def respond_to_requests(self, name):
    response = "HTTP/1.1 200 OK\r\nContent-Type:text/html;charset=utf8\r\n\r\n"
    try:
        with open(f"./static/index.html", "rb") as f:
            response += f.read()
        self.sock.send(response.encode())
    except IsADirectoryError:
        self.sock.send("没有这个文件".encode())


class WebSever:
    def __init__(self, host="", port=8888, html="./"):
        self.host = host
        self.port = port
        self.html = html
        self.addr = (host, port)
        self.sock = self.bind()
        self.rlist = [self.sock]
        self.wlist = []
        self.xlist = []

    def bind(self):
        socked = socket()
        socked.bind(self.addr)
        socked.setblocking(False)
        return socked

    def connect(self):
        connfd, addr = self.sock.accept()
        print(f"{addr}已链接")
        connfd.setblocking(False)
        self.rlist.append(connfd)

    def handle(self, connfd):
        data = connfd.recv(1024).decode()
        self.analysis = Analysis(connfd)
        self.analysis.analysis(data)
        self.rlist.remove(connfd)
        connfd.close()

    def start(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sock:
                    self.connect()
                else:
                    self.handle(r)


if __name__ == '__main__':
    httpsever = WebSever(host='0.0.0.0', port=7788, html="./")
    httpsever.start()
