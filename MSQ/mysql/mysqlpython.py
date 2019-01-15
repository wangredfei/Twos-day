import pymysql

class Mysqlpython:
    def __init__(self,database,host="localhost",
                      user="root",
                      password="123456",
                      charset="utf8",
                      port=3306):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.charset = charset
        self.port = port
    # 创建数据库连接对象和游标对象
    def open(self):
        self.db = pymysql.connect(host=self.host,
                      user=self.user,
                      password=self.password,
                      port=self.port,
                      database=self.database,
                      charset=self.charset)
        self.cur = self.db.cursor()
    # 关闭游标对象和数据库连接对象
    def close(self):
        self.cur.close()
        self.db.close()

    def zhixing(self,sql,L=[]):
        self.open()
        self.cur.execute(sql,L)
        self.db.commit()
        self.close()

    def all(self,sql,L=[]):
        self.open()
        # self.cur存放了所有的查询结果
        self.cur.execute(sql,L)
        result = self.cur.fetchall()
        self.close()
        return result








