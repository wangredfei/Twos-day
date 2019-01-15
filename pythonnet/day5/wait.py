import os 
from time import sleep

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    sleep(3)
    print("Child process %d exit"%os.getpid())
    os._exit(2)
else:
    # pid,status = os.wait() #阻塞
    pid,status=os.waitpid(-1,os.WNOHANG) #非阻塞
    print("pid:",pid)
    # print("status:",status)
    #获取退出状态
    print("status:",os.WEXITSTATUS(status))
    while True:
        pass 