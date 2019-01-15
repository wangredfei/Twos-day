# find.py
# 查询
import pymongo

# 1. 连接数据库
conn = pymongo.MongoClient("localhost",27017)
# 2. 列出所有数据库
dblist = conn.database_names()
db = "test"
# 判断库是否存在
if db in dblist:
    mydb = conn["test"] #获取数据库对象 
    mycol = mydb["acct"] #选择集合
    # 查询, 打印
    #docs = mycol.find({}, {"_id":0})
    docs = mycol.find({"acct_no":"622345111111"},
                  {"_id":0})
    for doc in docs:
        print(doc)
else:
    print("not found collection:", db)
conn.close()