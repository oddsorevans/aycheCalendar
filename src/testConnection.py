from pymongo import MongoClient

client = MongoClient("mongodb://Ayche:3Y8yqtb23lSdbVmf@ayche-shard-00-00-7twqa.mongodb.net:27017,ayche-shard-00-01-7twqa.mongodb.net:27017,ayche-shard-00-02-7twqa.mongodb.net:27017/test?ssl=true&replicaSet=Ayche-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database('Data')
records = db.users
print(records.count_documents({}))