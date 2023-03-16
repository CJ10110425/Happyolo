import pymongo
import re
client = pymongo.MongoClient("mongodb+srv://ze0966747312:a0966747312@cluster0.bf8bdil.mongodb.net/?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)
mydb=client["HappyYolo"]
mycol=mydb["Sustainable_Water_Profile"]





def store_profile(dict):
    mycol.insert_one(dict)

def  find_profile(user_id):
    return mycol.find_one({"User_Id":user_id })


def delete_profile(user_id):
    mycol.delete_one({"User_Id":user_id})

def update_Status(user_id,status):
    mycol.update_one({"User_Id":user_id},{"$set":{"Status":status}})


def update_Level(user_id,status):
    mycol.update_one({"User_Id":user_id},{"$set":{"Level":status}})


def update_name(user_id,name):
    mycol.update_one({"User_Id":user_id},{"$set":{"Name":name}})

def check_profil_exist(user_id):
    if find_profile(user_id) is None:
        return False
    else:
        return True
    

def find_password(user_id):
    IP=find_profile(user_id)
    password=IP["password"]
    return password

def check_account(user_id,account):

    if account=="Angel":
        update_Status(user_id,"password_logging")
        return "Angel~~\n請輸入密碼:"
    elif account=="Jerry":
        update_Status(user_id,"password_logging")
        return "Jerry~~\n請輸入密碼:"
    elif account=="淨彤":
        update_Status(user_id,"password_logging")
        return "淨彤~\n請輸入密碼:" 
    elif account=="Vera":
        update_Status(user_id,"password_logging")
        return "Vera~~\n請輸入密碼:"
    elif account=="育華":
        update_Status(user_id,"password_logging")
        return "育華~~\n請輸入密碼:"
    else:
        return "找不到此帳號"

def check_password(user_id,password):
    if password=="0919":
        update_Status(user_id,"Standard")
        update_Level(user_id,"manager")
        update_name(user_id,"jerry")
        return "jerry 歡迎回來~"
    elif password=="0502":
        update_Status(user_id,"Standard")
        update_Level(user_id,"manager")
        update_name(user_id,"淨彤")
        return "淨彤 歡迎回來~"
    elif password=="0120":
        update_Status(user_id,"Standard")
        update_Level(user_id,"manager")
        update_name(user_id,"Vera")
        return "Vera 歡迎回來~"
    elif password=="0626":
        update_Status(user_id,"Standard")
        update_Level(user_id,"manager")
        update_name(user_id,"育華")
        return "育華 歡迎回來~"
    elif password=="9411":
        update_Status(user_id,"Standard")
        update_Level(user_id,"manager")
        update_name(user_id,"Angel")
        return "Angel 歡迎回來~"
    else:
        return "密碼有誤~\n請再輸入一次"
    
    
