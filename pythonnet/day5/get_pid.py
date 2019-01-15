import os 
from time import sleep 

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    sleep(1)
    print("Child PID",os.getpid())
    print("Get parent PID",os.getppid())
else:
    print("Get child pid:",pid)
    print("Parent PID",os.getpid())