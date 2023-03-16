import pymongo
import re
client = pymongo.MongoClient("mongodb+srv://ze0966747312:a0966747312@cluster0.bf8bdil.mongodb.net/?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)
mydb=client["HappyYolo"]
mycol=mydb["client_data"]
from linebot.models import *


def insert_clienet_data(user_id,name):
      if mycol.find_one({"User_id":user_id}) is None:
            max=mycol.find_one({},sort=[("order",-1)])
            order=max["order"]+1
            dict={"User_id":user_id,"Name":name,"phone":"null","address":"null","install_date":"null","order":order}
            mycol.insert_one(dict)
      else:
         mycol.update_one({"User_id":user_id},{"$set":{"Name":name}})
            

def update_client_data_phone(user_id,phone):
       mycol.update_one({"User_id":user_id},{"$set":{"phone":phone}})

def select_date():
        action = DatetimePickerAction(
                label='選擇日期時間',
                data='action=buy&itemid=1',
                mode='datetime'
            )
        buttons_template = ButtonsTemplate(
                title='選擇日期時間',
                text='請選擇您要的日期時間',
                actions=[action]
            )
        template = TemplateSendMessage(
                alt_text='選擇日期時間',
                template=buttons_template
            )
        return template
        
def select_address():
        location_message = TemplateSendMessage(
            alt_text='請選擇位置',
            template=ButtonsTemplate(
            title='請選擇您要裝設地址',
            text='謝謝',
            actions=[
                LocationAction(
                label='點開查詢',
            )
        ]
    )
)

        return location_message

def confirm_client_name(name):
       confirm_template_message = TemplateSendMessage(
            alt_text='確定客戶名字',
            template=ConfirmTemplate(
                text=name,
                actions=[
                    PostbackAction(
                        label='確定',
                        data='action=register_2'
                    ),
                    PostbackAction(
                        label='寫錯了',
                        data='action=wrong_1'

                    )
                ]
            )
        )
       return confirm_template_message

def confirm_client_phone(phone):
       confirm_template_message = TemplateSendMessage(
            alt_text='確定客戶名字',
            template=ConfirmTemplate(
                text=str(phone),
                actions=[
                    PostbackAction(
                        label='確定',
                        data='action=register_3'
                    ),
                    PostbackAction(
                        label='寫錯了',
                        data='action=wrong_2'

                    )
                ]
            )
        )
       return confirm_template_message


def confirm_client_address(address):
       confirm_template_message = TemplateSendMessage(
            alt_text='確定客戶名字',
            template=ConfirmTemplate(
                text=str(address),
                actions=[
                    PostbackAction(
                        label='確定',
                        data='action=register_4'
                    ),
                    PostbackAction(
                        label='寫錯了',
                        data='action=wrong_3'

                    )
                ]
            )
        )
       return confirm_template_message


def confirm_client():
       confirm_template_message = TemplateSendMessage(
            alt_text='確定訪客要不要成為我們的客戶',
            template=ConfirmTemplate(
                text='確定要成為我們的客戶嗎',
                actions=[
                    PostbackAction(
                        label='確定',
                        data='action=Yes'
                    ),
                    PostbackAction(
                        label='按錯了',
                        data='action=No'

                    )
                ]
            )
        )
       return confirm_template_message

def update_client_data_address(user_id,address):
       mycol.update_one({"User_id":user_id},{"$set":{"address":address}})

def update_client_data_install_date(user_id,install_date):
        mycol.update_one({"User_id":user_id},{"$set":{"install_date":install_date}})

def confirm_client_install_date(date):
       confirm_template_message = TemplateSendMessage(
            alt_text='確定客戶安裝日期',
            template=ConfirmTemplate(
                text=str(date),
                actions=[
                    PostbackAction(
                        label='確定',
                        data='action=register_5'
                    ),
                    PostbackAction(
                        label='寫錯了',
                        data='action=wrong_4'

                    )
                ]
            )
        )
       return confirm_template_message
