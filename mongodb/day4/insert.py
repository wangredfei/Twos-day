# insert.py
# Mongodb插入操作
import pymongo

# 1. 建立连接
conn = pymongo.MongoClient("localhost",27017)

# 2. 列出所有数据库
dblist = conn.database_names()
db = "test"
if db in dblist:
    mydb = conn["test"]  # 获取数据库对象
    mycol = mydb["acct"] # 获取集合对象
    # 定义插入的内容
    mydict = {
        "acct_no": "622345888888",
        "acct_name": "David",
        "balance":3333.33
    }
    ret = mycol.insert_one(mydict)
    print(ret.inserted_id) # 打印新插入的ID号
else:
    print("db not found")
conn.close()