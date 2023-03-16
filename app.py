#載入LineBot所需要的套件
from ast import Store
from curses.ascii import isdigit
import re
from secrets import choice
from telnetlib import IP
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
app = Flask(__name__)
import dbprofile
import manager
import visitor
import copywriting
import datetime
import client_data
import customer_cop
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('RJA5Pi8oOuEUdfO4P7U8NOTYbmRJBu+xR5WjJUZuc4eUcqLEnLuKPXYCTXzU0K3W/AAzjhyx7tc6Tk6Ox5WV5idRdptNx4hxxc4umuWrNS0ZMIyjuF2acAKKj09/QbGlb02osfGsygV7g9Q4bEF+RgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('91103cfdd30156e0397687f9ab4f6d7f')

line_bot_api.push_message('U072f53bddc058e98772e7e785fda9274', TextSendMessage(text='續水\n———我們賣永續的水'))
ID='U072f53bddc058e98772e7e785fda9274'
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def is_number(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
def is_string(string):
    return isinstance(string,str)
#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg =event.message.text
    user_id = event.source.user_id
    Status="null"
    Level="null"
    reply="品澤還沒寫到喔"
    if dbprofile.check_profil_exist(user_id):#確認是否有使用者資料
        IP=dbprofile.find_profile(user_id)
        Status=IP["Status"]
        Level=IP["Level"]
        Name=IP["Name"]
    else:
        Profile={"User_Id":user_id,"Name":"Null","Status":"Standard","Level":"visitor"}
        dbprofile.store_profile(Profile)
        reply="已經幫你初始化啦"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
    

    if msg=="@管理者登錄":
        reply=manager.manager_logging(user_id,Status,Level) 
        line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
    elif Status=="account_logging":
        reply=dbprofile.check_account(user_id,msg)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
    elif Status=="password_logging":
        reply=dbprofile.check_password(user_id,msg)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
    
    
    if re.match(Level,"manager"):
        if re.match(msg,"@重新來過") and Level=="manager":
            reply=manager.refresh(user_id)
        
        if msg=="@管理者登出":
            flex_message=manager.manager_signout(user_id)
            reply=line_bot_api.reply_message(event.reply_token,flex_message)
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif Status=="signout":
            reply=manager.manager_signout_confirm(msg,user_id)
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        elif msg=="@更改關於我們":
            line_bot_api.reply_message(event.reply_token,TextSendMessage("請輸入想改的內容💡"))
            dbprofile.update_Status(user_id,"revising")
        elif Status=="revising":
            manager.update_about_us(msg)
            line_bot_api.reply_message(event.reply_token,TextSendMessage("修改完成\n謝謝"+Name+"\n我們又更進一步了"))
            dbprofile.update_Status(user_id,"Standard")

    if  re.match(Level,"visitor"):
        if re.match(msg,"💧"):
            reply=visitor.introduce()
            line_bot_api.reply_message(event.reply_token,reply)
        if re.match(msg,"馬上水一波"):
            reply=client_data.confirm_client()
            line_bot_api.reply_message(event.reply_token,reply)
        elif Status=="register_1":
            client_data.insert_clienet_data(user_id,msg)
            reply=client_data.confirm_client_name(msg)
            line_bot_api.reply_message(event.reply_token,reply)
        elif Status=="register_2":
            client_data.update_client_data_phone(user_id,msg)
            reply=client_data.confirm_client_phone(msg)
            line_bot_api.reply_message(event.reply_token,reply)
        if re.match(msg,"你們是誰？"):
            reply=copywriting.find_text("about_us")
            line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
        if re.match(msg,"請給我一張回饋單"):
            line_bot_api.reply_message(event.reply_token,TextSendMessage("已經幫您生成一張單子了\n請寫下您想說的話"))
            dbprofile.update_Status(user_id,"complaint")
        elif Status=="complaint":
            reply=customer_cop.insert_customer_cop(msg)
            reply=line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))
            dbprofile.update_Status(user_id,"Standard")
        


@handler.add(MessageEvent, message=LocationMessage)

def handle_location(event):
    user_id = event.source.user_id
    address = event.message.address
    address=text=address
    client_data.update_client_data_address(user_id,address)
    reply=client_data.confirm_client_address(address)
    line_bot_api.reply_message(event.reply_token,reply)

@handler.add(PostbackEvent)
def handle_postback(event):
    user_id = event.source.user_id
    IP=dbprofile.find_profile(user_id)
    Status=IP["Status"]
    Level=IP["Level"]
    if 'action=buy&itemid=1' in event.postback.data and Status=="register_4":          
        datetime_str = event.postback.params['datetime']
        datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
        reply_text = f'{datetime_obj.month}月{datetime_obj.day}日{datetime_obj.hour}點{datetime_obj.minute}分'
        client_data.update_client_data_install_date(user_id,reply_text)
        reply=client_data.confirm_client_install_date(reply_text)
        line_bot_api.reply_message(event.reply_token,reply)
    elif 'action=Yes'  in event.postback.data and Status=="Standard":
        dbprofile.update_Status(user_id,"register_1")
        line_bot_api.reply_message(event.reply_token, TextSendMessage("請輸入您的名字(全名):"))
    elif 'action=No'  in event.postback.data and Status=="Standard":
        line_bot_api.reply_message(event.reply_token, TextSendMessage("謝謝你～🥹"))
    elif 'action=register_2'  in event.postback.data and Status=="register_1":
        dbprofile.update_Status(user_id,"register_2")
        line_bot_api.reply_message(event.reply_token, TextSendMessage("請輸入您的電話號碼\n(格式為09XX XXX XXX)\n可以不用空格"))
    elif 'action=wrong_1'  in event.postback.data and Status=="register_1":
        line_bot_api.reply_message(event.reply_token, TextSendMessage("請輸入您的名字(全名):"))
    elif 'action=register_3'  in event.postback.data and Status=="register_2":
        dbprofile.update_Status(user_id,"register_3")
        reply=client_data.select_address()
        line_bot_api.reply_message(event.reply_token,reply)
    elif 'action=wrong_2'  in event.postback.data and Status=="register_2":
        line_bot_api.reply_message(event.reply_token, TextSendMessage("請輸入您的電話號碼\n(格式為09XX XXX XXX)\n可以不用空格"))
    elif 'action=register_4'  in event.postback.data and Status=="register_3":
        dbprofile.update_Status(user_id,"register_4")
        reply=client_data.select_date()
        line_bot_api.reply_message(event.reply_token,reply)
    elif 'action=wrong_3'  in event.postback.data and Status=="register_3":
        reply=client_data.select_address()
        line_bot_api.reply_message(event.reply_token,reply)
    elif 'action=register_5'  in event.postback.data and Status=="register_4":
        dbprofile.update_Status(user_id,"register_5")
        line_bot_api.reply_message(event.reply_token, TextSendMessage("已幫你初始化一個儲水器～～～💦💦💦"))
        pass#開始模擬
    elif 'action=wrong_4' in event.postback.data and Status=="register_4":
        reply=client_data.select_date()
        line_bot_api.reply_message(event.reply_token,reply)
    
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)