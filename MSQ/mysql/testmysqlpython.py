from mysqlpython import Mysqlpython

# 创建对象
sqlh = Mysqlpython("db5")
sqlh.zhixing('update t1 set score=100')

r = sqlh.all('select * from t1')
print(r)




