# insert_many.py
# Mongodb插入多行操作
import pymongo

# 1. 建立连接
conn = pymongo.MongoClient("localhost",27017)

# 2. 列出所有数据库
dblist = conn.database_names()
db = "test"
if db in dblist:
    mydb = conn["test"]  # 获取数据库对象
    mycol = mydb["acct"] # 获取集合对象
    # 定义插入的内容, 多笔传入列表参数
    mydict = [
      {"acct_no":"622345777", "acct_name":"Kevin"},
      {"acct_no":"622345666", "acct_name":"Emma"}
    ]
    ret = mycol.insert_many(mydict)# 插入多笔
    print(ret.inserted_ids) # 打印新插入的ID号
else:
    print("db not found")
conn.close()