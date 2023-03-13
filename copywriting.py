import pymongo
import re
client = pymongo.MongoClient("mongodb+srv://ze0966747312:a0966747312@cluster0.bf8bdil.mongodb.net/?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)
mydb=client["HappyYolo"]
mycol=mydb["copywriting"]

def update_copywriting(category,text):
    mycol.update_one({"category":category},{"$set":{"text":text}})

def  find_text(category):
    IP=mycol.find_one({"category":category })
    return IP["text"]
