import  os 
from time import sleep 

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    sleep(3)
    print("New process")
else:
    sleep(4)
    print("Old process")

print("====The end====")
