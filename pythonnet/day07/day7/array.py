from multiprocessing import Process,Array 
import time 

#开辟共享内存,存入整数列表
# shm = Array('i',[1,2,3,4,5])

#开辟5个整形空间
# shm = Array('i',5)

#存入字符串
shm = Array('c',b'hello')

def fun():
    for i in shm:
        print(i)
    shm[0] = b'H'

p = Process(target = fun)
p.start()
p.join()

for i in shm:
    print(i,end=' ')
print()
print(shm.value) #打印字符串


