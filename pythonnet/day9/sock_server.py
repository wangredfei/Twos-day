from socketserver import * 

#创建服务器类
# class Server(ForkingMixIn,TCPServer):
# class Server(ThreadingMixIn,TCPServer):
class Server(ThreadingTCPServer):
    pass 

#处理请求类
class Handler(StreamRequestHandler):
    #重写handle方法
    def handle(self):
        print("Connect from:",self.client_address)
        while True:
            #self.request==>accept 返回的连接套接字 
            data = self.request.recv(1024)
            if not data:
                break 
            print(data.decode())
            self.request.send(b'Receive')

#创建服务器对象
server = Server(('0.0.0.0',8888),Handler)
server.serve_forever() #启动服务

