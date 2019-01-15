# delete.py
# 删除数据
import pymongo
# 连接数据库
conn = pymongo.MongoClient("localhost",27017)
# 列出所有数据库
dblist = conn.database_names()
db = "test"
if db in dblist:
    mydb = conn["test"] # 获取数据库对象
    mycol = mydb["acct"] # 获取集合对象
    myquery = {"acct_no":"622345666",
                "acct_name":"Emma"}
    ret = mycol.delete_one(myquery)
    print("删除笔数:%d" % ret.deleted_count)
else:
    print("db not found")
conn.close()







