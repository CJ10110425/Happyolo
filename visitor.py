import dbprofile
from linebot.models import *
import re


def introduce():    
    carousel_template_message = TemplateSendMessage(
                alt_text='pass',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url='https://png.pngtree.com/png-clipart/20200225/original/pngtree-vector-of-water-droplets-falling-down-to-the-ground-water-saving-png-image_5295426.jpg',
                            title='續水',
                            text='———我們賣永續的水',
                            actions=[
                                MessageAction(
                                    label='瞭解更多',
                                    text='馬上水一波'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://png.pngtree.com/png-clipart/20200710/original/pngtree-law-and-justice-logo-png-image_4136187.jpg',
                            title='水利相關法律',
                            text='———讓您更了解',
                            actions=[
                                URIAction(
                                    label='馬上查看',
                                    uri='https://law.moj.gov.tw/LawClass/LawParaDeatil.aspx?pcode=J0110001&bp=4'
                                )
                            ]
                        ),CarouselColumn(
                            thumbnail_image_url='https://png.pngtree.com/png-clipart/20220303/original/pngtree-about-our-company-interface-png-image_7390103.png',
                            title='嘿疲YOLO乳',
                            text='——— Building a Better World',
                            actions=[
                                MessageAction(
                                    label='關於我們',
                                    text='你們是誰？'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://png.pngtree.com/png-clipart/20221006/original/pngtree-customer-feedback-png-image_8661266.png',
                            title='建議箱',
                            text='———您的每一個建議，都讓我們激動不已，促使我們不斷奮進',
                            actions=[
                                MessageAction(
                                    label='馬上回饋',
                                    text='請給我一張回饋單'
                                )
                            ]
                        )
                    ]
                )
            )
    return carousel_template_message