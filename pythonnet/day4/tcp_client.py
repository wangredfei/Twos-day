from socket import *

#创建tcp套接字
sockfd = socket()

#发起连接
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

#消息收发
while True:
    data = input(">>")
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("From server:",data.decode())

sockfd.close()