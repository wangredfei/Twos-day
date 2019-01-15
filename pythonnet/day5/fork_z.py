import os 
from time import sleep 

pid = os.fork()

if pid == 0:
    print("Child PID",os.getpid())
    os._exit(1)
else:
    print("Parent process")
    sleep(20)

