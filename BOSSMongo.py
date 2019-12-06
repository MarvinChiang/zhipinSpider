from BOSSBase import *
import  pymongo
MONGO_URL='localhost'
client = pymongo.MongoClient(MONGO_URL)
db =client[MONGO_DB]
def save_to_mongo(result):
    try:
        db[MONGO_TABLE].insert_one(result)
        print('mongoDB保存成功:')
    except Exception:
        print('保存失败')