from threading import Thread,currentThread
from time import sleep 

def fun():
    print("线程属性测试")
    sleep(3)
    #获取当前线程对象
    print("%s线程执行完毕"%currentThread().getName())

t = Thread(target=fun,name='Tarena')

t.setDaemon(True)
# t.daemon = True 

t.start()

#线程名称
t.setName("Tedu")
print("Thread name:",t.name)
print("Get Thread name:",t.getName())

print("is alive : ",t.is_alive()) #线程状态

print("Daemon:",t.isDaemon())

# t.join()
print("=========main thread==========")

