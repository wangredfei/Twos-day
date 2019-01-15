from threading import Thread,Lock 

a = b = 0 
lock = Lock()

def fun():
    while True:
        lock.acquire()  #加锁
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release()  #解锁

t = Thread(target = fun)
t.start()

while True:
    with lock:  #加锁
        a += 1
        b += 1

t.join()
