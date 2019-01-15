import pymysql

conn = pymysql.connect(host="localhost",
                       user="root",
                       password="123456",
                       database="db5",
                       charset="utf8",
                       port=3306)
cur = conn.cursor()
try:
    # 增加
    ins = 'insert into t1(name,score) values\
           ("小姐姐",100)'
    cur.execute(ins)
    # 修改
    upd = 'update t1 set score=100 where name\
           ="李白"'
    cur.execute(upd)
    # 删除
    dele = 'delete from t1 where name="杜甫"'
    cur.execute(dele)
    conn.commit()
except:
    conn.rollback()
    print("出现异常")

cur.close()
conn.close()












