from socket import *
import struct 

ADDR = ('127.0.0.1',8888)
s = socket(AF_INET,SOCK_DGRAM) 

# st = struct.Struct('i4sf')

while True:
    id = input("id:")
    name = input("name:")
    n = len(name)
    height = input("height:")

    fmt = "i%dsf"%n
    s.sendto(fmt.encode(),ADDR) #先发送格式

    data=struct.pack(fmt,int(id),\
    name.encode(),float(height))
    s.sendto(data,ADDR)  #发送数据




