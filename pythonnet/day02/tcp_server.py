import socket 

#创建tcp套接字
sockfd=socket.socket(\
socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
sockfd.bind(('0.0.0.0',8866))

#设置监听
sockfd.listen(5)

while True:
    print("Waiting for connect...")
    #处理客户端连接
    try:
        connfd,addr = sockfd.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        break
    #收发消息
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print("Receive:",data.decode())
        n = connfd.send("Hello Kitty".encode())
        print("Send %d bytes"%n)
    connfd.close()

#关闭套接字
sockfd.close()
