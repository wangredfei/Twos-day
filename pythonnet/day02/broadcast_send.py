from socket import * 
from time import sleep 

#设置广播地址
dest = ('192.168.56.255',9999)

s = socket(AF_INET,SOCK_DGRAM)

#设置可以发送广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(2)
    s.sendto("往后余生,风雪是你".encode(),dest)
s.close()



