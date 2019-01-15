import os,sys 

# os._exit(0)

try:
    sys.exit("进程退出")
except SystemExit:
    pass

print("Process end")