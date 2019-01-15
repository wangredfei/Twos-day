import multiprocessing as mp 
from time import sleep,ctime 

a = 1

#进程函数
def fun():
    print("执行子进程")
    sleep(2)
    global a
    print("a = ",a)    
    a = 10000
    print("子进程执行完毕")

#创建进程对象
p = mp.Process(target = fun)
#启动进程
p.start()

for i in range(3):
    sleep(1)
    print(ctime())

#回收进程
p.join()

print("parent a:",a)

