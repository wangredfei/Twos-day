# show_dbs.py
# 显示mongo服务器上所有的数据库
import pymongo

# 1. 建立连接  MongoClient
# conn = pymongo.MongoClient(
#            "mongodb://localhost:27017")
conn = pymongo.MongoClient("localhost", 27017)

# 2. 获取数据库列表
#dblist = conn.list_database_names()
dblist = conn.database_names()
for db in dblist:  # 遍历, 打印
    print(db)

# 3. 关闭数据库
conn.close()
print("数据库已关闭")