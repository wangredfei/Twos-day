#生成器函数
def fun():
    print("启动生成器")
    # for i in range(5):
    #     yield i
    yield from range(5)
    print("结束生成器")

#生成器对象
g = fun()
while True:
    try:
        print(next(g))
        print("=========")
    except:
        break 
