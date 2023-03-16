import dbprofile
from linebot.models import *
import re
import pymongo
client = pymongo.MongoClient("mongodb+srv://ze0966747312:a0966747312@cluster0.bf8bdil.mongodb.net/?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)
mydb=client["HappyYolo"]
mycol=mydb["copywriting"]


def manager_logging(user_id,Status,Level):
    if Status=="Standard" and Level=="visitor":
        dbprofile.update_Status(user_id,"account_logging")
        return "請輸入您的帳號\n(帳號為您的姓名)"
    elif Level=="manager":
        return ("你已經登錄過啦")
    
def manager_signout(user_id):
    flex_message=TextSendMessage(
                text="確定要退出嗎",
                quick_reply=QuickReply(items=[
                QuickReplyButton(action=MessageAction(label="確定",text="@管理者確定登出")),
                QuickReplyButton(action=MessageAction(label="不小心按錯",text="@管理者不登出"))
            ]))
    dbprofile.update_Status(user_id,"signout")
    return flex_message 

def manager_signout_confirm(msg,user_id):
    if re.match(msg,"@管理者確定登出"):
            dbprofile.update_Status(user_id,"Standard")
            dbprofile.update_Level(user_id,"visitor")
            return "已登出"
    elif re.match(msg,"@管理者不登出"):
            return "已取消登出"
    
def refresh(user_id):
     dbprofile.update_Status(user_id,"Standard")
     dbprofile.update_Level(user_id,"visitor")
     dbprofile.update_name(user_id,"null")
     return "你重新做人啦"


def update_about_us(text):
    mycol.update_one({"category":"about_us"},{"$set":{"text":text}})