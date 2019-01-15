'''
name: dict 
modules: pymysql 
This is a test dict for AID
'''
from socket import * 
import pymysql 
import os,sys 
from threading import Thread
import time 

#定义全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
DICT_TEXT = './dict.txt'

#处理僵尸进程
def zombie():
    os.wait()

#搭建网络
def main():
    #创建数据库连接
    db = pymysql.connect('localhost',\
    'root','123456','dict')

    #创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print("Error:",e)
            continue

        #创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()
            do_child(c,db)  #子进程函数
            os._exit(0)
        else:
            c.close()
            t = Thread(target=zombie)
            t.setDaemon(True)
            t.start()
            continue

#具体处理客户端请求
def do_child(c,db):
    while True:
        #接收客户端请求
        data = c.recv(1024).decode()
        print(c.getpeername(),":",data)
        if not data or data[0]=='E':
            c.close()
            sys.exit()
        elif data[0] == 'R':
            do_register(c,db,data)
        elif data[0] == 'L':
            do_login(c,db,data)
        elif data[0] == 'Q':
            do_query(c,db,data)
        elif data[0] == 'H':
            do_history(c,db,data)

def do_history(c,db,data):
    name = data.split(' ')[1]
    cursor = db.cursor()
    sql="select * from hist where name='%s'"%name
    cursor.execute(sql)
    r = cursor.fetchall()

    if not r:
        c.send(b'FALL')
        return
    else:
        c.send(b'OK')
        time.sleep(0.1)
    
    #发送历史记录
    for i in r:
        msg="%4s   %4s   %s"%(i[1],i[2],i[3])
        c.send(msg.encode())
        time.sleep(0.1)
    c.send(b'##')


def do_query(c,db,data):
    l = data.split(' ')
    name = l[1]
    word = l[2]

    def insert_history():
        cursor = db.cursor()
        tm = time.ctime()
        sql="insert into hist (name,word,time)\
         values ('%s','%s','%s')"%(name,word,tm)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    #使用单词本查找
    try:
        f = open(DICT_TEXT)
    except Exception as e:
        c.send(b'FALL')
        return 
    for line in f:
        tmp = line.split(' ')[0]
        if tmp > word:
            c.send(b'FALL')
            f.close()
            return
        elif tmp == word: #查到单词
            c.send(line.encode())
            f.close()
            insert_history() #插入历史记录
            return 
    c.send(b'FALL')
    f.close()

    


def do_register(c,db,data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql="select * from user where name='%s'"%name 
    cursor.execute(sql)
    r = cursor.fetchone()
    #r不为None表示该用户已存在
    if r != None:
        c.send(b'EXISTS')
        return 

    #插入用户
    sql="insert into user (name,passwd) values \
    ('%s','%s')"%(name,passwd)

    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        db.rollback()
        c.send(b'FALL')

def do_login(c,db,data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql="select * from user where \
    name='%s' and passwd='%s'"%(name,passwd)
    
    #查找用户
    cursor.execute(sql)
    r = cursor.fetchone()
    if r == None:
        c.send(b'FALL')
    else:
        c.send(b'OK')

main()