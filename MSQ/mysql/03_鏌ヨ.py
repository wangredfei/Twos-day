import pymysql

db = pymysql.connect(host="localhost",
                     user="root",
                     password="123456",
                     database="db5",
                     charset="utf8")
cursor = db.cursor()
sel = 'select * from t1'
cursor.execute(sel)
# fetchone
One = cursor.fetchone()
print(One)
print("*" * 30)

# fetchmany(2)
# 结果为大元组,每一条记录为一个小元组
Many = cursor.fetchmany(2)
for m in Many:
    print(m)
print("*" * 30)

# fetchall()
# 结果为大元组,每一条记录为一个小元组
All = cursor.fetchall()
for m in All:
    print(m)

db.commit()
cursor.close()
db.close()




















