import pymongo
client = pymongo.MongoClient("mongodb+srv://ze0966747312:a0966747312@cluster0.bf8bdil.mongodb.net/?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)
mydb=client["HappyYolo"]
mycol=mydb["customer_complaint"]


def insert_customer_cop(text):
        max=mycol.find_one({},sort=[("order",-1)])
        order=max["order"]+1
        dict={"text":text,"order":order}
        mycol.insert_one(dict)
        return ("感謝您的寶貴意見\n您是第"+str(order)+"給我們想法的人\nhappy~")
