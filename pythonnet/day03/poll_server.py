from socket import *
from select import * 

#创建套接字作为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

#创建poll对象
p = poll()

#建立查找字典
fdmap = {s.fileno():s}

#注册IO
p.register(s,POLLIN|POLLERR)

#循环监控
while True:
    events = p.poll() #等待IO发生
    for fd,event in events:
        if fd == s.fileno():
            c,addr =fdmap[fd].accept()
            print("Connect from",addr)
            #添加新的关注IO
            p.register(c,POLLIN|POLLHUP)
            fdmap[c.fileno()]=c 
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd) 
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print("Receive:",data.decode())
                fdmap[fd].send(b"Receive")

        

