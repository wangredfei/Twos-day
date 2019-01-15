from multiprocessing import Pool 
from time import sleep,ctime 

def worker(msg):
    sleep(2)
    print(msg)
    return msg

#创建进程池对象
pool = Pool(processes = 4)

result = []
#向进程池添加事件
for i in range(10):
    msg = "hello %d"%i
    # r = pool.apply_async(func=worker,args=(msg,))
    # result.append(r)
    
    #将事件同步方式放入进程池
    pool.apply(func=worker,args=(msg,))

#关闭进程池
pool.close()
#回收进程池
pool.join()
print("========================")
# for i in result:
#     print(i.get())