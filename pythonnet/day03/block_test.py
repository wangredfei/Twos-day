from socket import *
from time import sleep,ctime 

#tcp套接字
sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(3)

#设置非阻塞状态
# sockfd.setblocking(False)
#设置超时时间
sockfd.settimeout(5)

while True:
    print("Waiting for connect...")
    try:
        connfd,addr = sockfd.accept()
    except BlockingIOError:
        sleep(2)
        print(ctime())
        continue 
    except timeout:
        print("超时等待5秒..")
        continue
    else:
        data = connfd.recv(1024).decode()
        print(data)
        connfd.send(b"Receive message")
        break 

sockfd.close()
    