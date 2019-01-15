from threading import Event 

#创建事件对象
e = Event() 

e.set() #设置e
e.clear()
print(e.is_set()) #判断当前状态
e.wait()

print("**********************")
