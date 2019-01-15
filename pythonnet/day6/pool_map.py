from multiprocessing import Pool 
import time 

def fun(n):
    time.sleep(1)
    return n * n 

pool = Pool()

#使用map向进程池加入事件
r = pool.map(fun,range(6))
pool.close()
pool.join()
print(r)