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
    else:
        Profile={"User_Id":user_id,"Name":"Null","Status":"Standard","Level":"visitor"}
        dbprofile.store_profile(Profile)
        reply="已經幫你初始化啦"
    

    if msg=="@管理者登錄":
        reply=manager.manager_logging(user_id,Status,Level)  
    elif Status=="account_logging":
        reply=dbprofile.check_account(user_id,msg)
    elif Status=="password_logging":
        reply=dbprofile.check_password(user_id,msg)
    
    
    if re.match(Level,"manager"):
        if re.match(msg,"@重新來過") and Level=="manager":
            reply=manager.refresh(user_id)
        
        if msg=="@管理者登出":
            flex_message=manager.manager_signout(user_id)
            line_bot_api.reply_message(event.reply_token,flex_message)
        elif Status=="signout":
            reply=manager.manager_signout_confirm(msg,user_id)

    if  re.match(Level,"visitor"):
        if re.match(msg,"💧"):
            reply=visitor.introduce()
            line_bot_api.reply_message(event.reply_token,reply)
        if re.match(msg,"馬上水一波"):
            
            pass
        if re.match(msg,"你們是誰？"):
            reply=copywriting.find_text("about_us")
            DatetimePickerAction
        if msg== "選擇日期時間":
            reply=client_data.select_date()
            line_bot_api.reply_message(
                event.reply_token,
                reply
            )
        if re.match("選擇地點",msg):
            reply=client_data.select_address()
            line_bot_api.reply_message(event.reply_token, reply)


        
    
    line_bot_api.reply_message(event.reply_token,TextSendMessage(reply))

@handler.add(MessageEvent, message=LocationMessage)
def handle_location(event):
    latitude = event.message.latitude
    longitude = event.message.longitude
    address = event.message.address

    # 回覆消費者
    reply_message = f"您所在的位置經度為{latitude}，緯度為{longitude}，地址為{address}"
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_message))

@handler.add(PostbackEvent)
def handle_postback(event):
    # if 'action=buy&itemid=1' in event.postback.data:
    #     datetime_str = event.postback.params['datetime']
    #     datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
    #     reply_text = f'您選擇的日期時間為：{datetime_obj.month}月{datetime_obj.day}日{datetime_obj.hour}點{datetime_obj.minute}分'
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))
    if 'action=buy&itemid=1' in event.postback.data:
        client_data.insert_data(event.postback.data)
        latitude = event.postback.params['latitude']
        longitude = event.postback.params['longitude']
        address = event.postback.params['address']
        reply_text = f'您選擇的位置為：{address} (緯度：{latitude}，經度：{longitude})'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)