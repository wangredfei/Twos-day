import socket 

#创建tcp套接字
sockfd=socket.socket(\
socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('0.0.0.0',8866))

#设置监听
sockfd.listen(5)

print("Waiting for connect...")
#处理客户端连接
connfd,addr = sockfd.accept()
print("Connect from",addr)

#收发消息
data = connfd.recv(1024)
print("Receive:",data.decode())

n = connfd.send("Hello Kitty".encode())
print("Send %d bytes"%n)

#关闭套接字
connfd.close()
sockfd.close()
