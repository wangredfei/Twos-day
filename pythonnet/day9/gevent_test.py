import gevent
from time import sleep 

def foo(a,b):
    print("Running in  foo",a,b)
    gevent.sleep(2)
    print("foo end")

def bar():
    print("Running in  bar")
    gevent.sleep(3)
    print("bar end")

f = gevent.spawn(foo,1,2)
b = gevent.spawn(bar)
gevent.joinall([f,b])
