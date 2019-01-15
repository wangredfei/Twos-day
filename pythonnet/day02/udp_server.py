from socket import * 

#创建UDP套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#绑定地址
sockfd.bind(('0.0.0.0',8888))

#收发消息
while True:
    data,addr = sockfd.recvfrom(1024)
    print("Receive from",addr,data.decode())
    sockfd.sendto(b"Thanks for your message",\
    addr)

sockfd.close()