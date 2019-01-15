import os 
from time import sleep 

filename = "./test.jpg"

#获取大小
size = os.path.getsize(filename)

# f = open(filename,'rb')

#上半部分
def copy1():
    f = open(filename,'rb')
    fw = open('1.jpg','wb')
    n = size // 2
    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()

#下半部分
def copy2():
    f = open("./test.jpg",'rb')
    fw = open("2.jpg",'wb')
    f.seek(size//2,0)
    while True:
        data = f.read(1024)
        if not data:
            break 
        fw.write(data)
    f.close()
    fw.close() 

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    sleep(1)
    copy1()
else:
    copy2()