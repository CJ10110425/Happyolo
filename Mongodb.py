import pymongo

client = pymongo.MongoClient("mongodb+srv://ze0966747312:a0966747312@cluster0.bf8bdil.mongodb.net/?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)
mydb=client["Work"]
mycol=mydb["data"]


def store_group_id(dict):
    mycol.insert_one(dict)

def check_profil_exist(group_id):
    if find_profile(group_id) is None:
        return False
    else:
        return True
    
def  find_profile(group_id):
    return mycol.find_one({ "group_id":group_id })
