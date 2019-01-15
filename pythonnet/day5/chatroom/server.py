#coding=utf-8
'''
chat room
env : python3.5
socket and fork
'''
from socket import *
import os,sys 

def do_login(s,user,name,addr):
    if (name in user) or name == "管理员":
        s.sendto('\n该用户已存在'.encode(),addr)
        return 
    s.sendto(b'OK',addr)

    #通知其他人
    msg = "\n欢迎 %s 进入聊天室"%name 
    for i in user:
        s.sendto(msg.encode(),user[i])
    #加入用户
    user[name] = addr 

def do_chat(s,user,name,text):
    msg = "\n%s 说:%s"%(name,text)
    for i in user:
        #发送给其他人
        if i != name:
            s.sendto(msg.encode(),user[i])

def do_quit(s,user,name):
    msg = "\n%s 退出了聊天室"%name 
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b'EXIT',user[name])
    del user[name]

def do_request(s):
    #存储用户 {'zhangsan':('127.0.0.1',8888)}
    user={}
    while True:
        msg,addr = s.recvfrom(1024)
        msgList = msg.decode().split(' ')
        #区分请求类型
        if msgList[0] == 'L':
            do_login(s,user,msgList[1],addr)
        elif msgList[0] == 'C':
            #重新组织消息
            text = ' '.join(msgList[2:])
            do_chat(s,user,msgList[1],text)
        elif msgList[0] == 'Q':
            do_quit(s,user,msgList[1])

#创建网络连接
def main():
    ADDR = ('0.0.0.0',8888)
    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    pid = os.fork()
    if pid < 0:
        print("创建进程失败")
        return 
    #子进程发送管理员消息
    elif pid == 0:
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员 %s"%msg
            #发送给父进程处理
            s.sendto(msg.encode(),ADDR)
    #父进程处理客户端请求
    else:
        do_request(s)


main()
