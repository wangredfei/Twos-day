'''在db5.t1表中插入1条记录'''
import pymysql

# 创建数据库连接对象
db = pymysql.connect("localhost","root",
                     "123456","db5",
                     charset="utf8")
# 利用数据库连接对象创建1个游标对象
cursor = db.cursor()
# 执行sql命令
cursor.execute('insert into t1(name,score)\
                values("王维",88)')
# 提交到数据库执行
db.commit()
print("ok")
# 关闭游标对象
cursor.close()
# 关闭数据库连接对象
db.close()











