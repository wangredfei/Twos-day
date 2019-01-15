from threading import Thread,Event 
from time import sleep 

s = None #作为通信变量
e = Event()

def bar():
    print("Bar 拜山头")
    sleep(0.5)
    global s 
    s = "天王盖地虎"
    e.set()  #让主线程执行判断
    
b = Thread(target=bar)
b.start()

print("说对口令就是自己人")
e.wait(3)  #阻塞等待,分支线程说完口令再判断
if s == "天王盖地虎":
    print("确认过眼神,你是对的人")
else:
    print("打死他")

b.join()

