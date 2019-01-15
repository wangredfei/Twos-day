# update.py
# 修改数据
import pymongo

# 连接数据库
conn = pymongo.MongoClient("localhost",27017)
# 列出所有数据库
dblist = conn.database_names()
db = "test"  # 操作的数据库
if db in dblist:
    mydb = conn["test"] # 获取数据库对象
    mycol = mydb["acct"] # 获取集合对象
    # 修改
    myquery = {"acct_no":"622345111111"}
    new_values = {"$set": {"balance":99.99}}
    ret = mycol.update_one(myquery, new_values)
    print("修改笔数:%d" % ret.modified_count)
else:
    print("db not found")

conn.close()