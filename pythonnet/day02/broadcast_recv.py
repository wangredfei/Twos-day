from socket import *

s = socket(AF_INET,SOCK_DGRAM)
#设置可以接收广播
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('0.0.0.0',9999))

while True:
    try:
        msg,addr = s.recvfrom(1024)
        print("广播:",msg.decode())
    except KeyboardInterrupt:
        break
s.close()






