from socket import *
import struct

s = socket(AF_INET,SOCK_DGRAM)
s.bind(('0.0.0.0',8888))

#接收数据格式
# st = struct.Struct("i32sf")

while True:
    data,addr = s.recvfrom(128) #接收格式
    fmt = data.decode()

    data,addr = s.recvfrom(1024) #接收数据
    data = struct.unpack(fmt,data)  #按照格式转换
    print(data)

s.close()

