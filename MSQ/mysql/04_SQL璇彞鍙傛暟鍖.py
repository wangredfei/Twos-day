import pymysql

db = pymysql.connect(host="localhost",
                     user="root",
                     password="123456",
                     charset="utf8")
cursor = db.cursor()
cursor.execute('use db5')

name = input("请输入学生姓名:")
score = input("请输入学生成绩:")

try:
    ins = 'insert into t1(name,score) values(%s,%s)'
    # 此方法不推荐使用
    # ins = "insert into t1(name,score) \
    # values('%s','%s')" % (name,score)
    # cursor.execute(ins)
    # execute中第二个参数一定要为列表
    cursor.execute(ins,[name,score])
    db.commit()
    print("添加成功")
except:
    db.rollback()

cursor.close()
db.close()












