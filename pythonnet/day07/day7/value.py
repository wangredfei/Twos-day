from multiprocessing import Process,Value 
import time 
import random 

#创建共享内存
money = Value('i',5000)

#挣钱
def boy():
    for i in range(30):
        time.sleep(0.2)
        #对value属性操作即操作共享内存
        money.value+=random.randint(1,1500)

def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value-=random.randint(100,1200)

b = Process(target = boy)
g = Process(target = girl)
b.start()
g.start()
b.join()
g.join()

print("一个月余额:",money.value)

