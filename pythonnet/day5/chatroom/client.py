from socket import * 
import os,sys 

def send_msg(s,name,ADDR):
    while True:
        try:
            text = input("发言:")
        except KeyboardInterrupt:
            text = "quit"

        if text == 'quit':
            msg = "Q " + name 
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        if data.decode() == "EXIT":
            os._exit(0)
        print(data.decode()+'\n发言:',end='')

#创建套接字
def main():
    #从命令行输入服务端地址
    if len(sys.argv) < 3:
        print("argv is error!")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)

    s = socket(AF_INET,SOCK_DGRAM)

    while True:
        name = input("请输入姓名:")
        msg = "L " + name 
        #给服务器发送
        s.sendto(msg.encode(),ADDR)
        #接收反馈
        data,addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break 
        else:
            print(data.decode())
    #创建父子进程
    pid = os.fork()
    if pid < 0:
        sys.exit("创建进程失败")
    elif pid == 0:
        send_msg(s,name,ADDR)
    else:
        recv_msg(s)

main()