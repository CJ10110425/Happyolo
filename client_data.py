import pymongo
import re
client = pymongo.MongoClient("mongodb+srv://ze0966747312:a0966747312@cluster0.bf8bdil.mongodb.net/?retryWrites=true&w=majority",tls=True,tlsAllowInvalidCertificates=True)
mydb=client["HappyYolo"]
mycol=mydb["client_data"]
import dbprofile
from linebot.models import *
import re


def insert_data(data):
      dict={"msg":data}
      mycol.insert_one(dict)


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
            title='請選擇位置',
            text='請分享您的位置',
            actions=[
                LocationAction(
                label='分享位置',
            )
        ]
    )
)

        return location_message
