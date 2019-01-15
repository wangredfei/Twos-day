from socket import * 

s = socket()

#设置端口重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('192.168.56.131',8888))

print("family:",s.family) #地址类型
print("type:",s.type) #套接字类型

#获取绑定地址
print("sockname:",s.getsockname())

#文件描述符
print("fileno:",s.fileno())

#获取选项值
print("get opt:",\
s.getsockopt(SOL_SOCKET,SO_REUSEADDR))


s.listen(3)
c,addr = s.accept()

#获取连接端地址
print("getpeername:",c.getpeername())
c.recv(1024)