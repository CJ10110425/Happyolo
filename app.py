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

line_bot_api.push_message('U072f53bddc058e98772e7e785fda9274', TextSendMessage(text='續水\n———我們賣永續的水\n更新啦'))
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
        reply="已經幫你建立您的個人檔案，‘再按一次"
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
        if re.match(msg,"為我解答"):
            reply=visitor.subject_4()
            line_bot_api.reply_message(event.reply_token,reply)
        elif re.match(msg,"瞭解更多簡介"):
            reply=visitor.introduction()
            line_bot_api.reply_message(event.reply_token,reply)
        elif re.match(msg,"瞭解更多選題"):
            reply=visitor.chose_topic()
            line_bot_api.reply_message(event.reply_token,reply)
        elif re.match(msg,"瞭解更多市場 & 優勢"):
            reply=visitor.market_advantage()
            line_bot_api.reply_message(event.reply_token,reply)
        elif re.match(msg,"瞭解更多運作模式"):
            reply=visitor.market_operation()
            line_bot_api.reply_message(event.reply_token,reply)
        elif re.match(msg,"瞭解更多商業模式"):
            reply=visitor.business_model()
            line_bot_api.reply_message(event.reply_token,reply)
        elif re.match(msg,"瞭解更多市場區隔"):
            reply=visitor.market_segment()
            line_bot_api.reply_message(event.reply_token,reply)
        elif re.match(msg,"瞭解更多預算部分"):
            reply=visitor.Budget()
            line_bot_api.reply_message(event.reply_token,reply)
        elif re.match(msg,"瞭解更多重點問題"):
            reply=visitor.important_que()
            line_bot_api.reply_message(event.reply_token,reply)
        if re.match(msg,"給我看看"):
            image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/simgad/8791108576365732220',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
            line_bot_api.reply_message(event.reply_token,image_message)
        if re.match(msg,"Happy"):
            line_bot_api.reply_message(event.reply_token,VideoSendMessage(
		    original_content_url='https://stream.mux.com/nR77024QBteG8ofTUpxtlCYNBTSeGT00viuZ4KGDB2NpU.m3u8?redundant_streams=true', 
		    preview_image_url='https://tpc.googlesyndication.com/simgad/8791108576365732220' 
	    ))
        elif re.match(msg,"YOLO"):
            flex_message = FlexSendMessage(
            alt_text='名片',
            contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://tpc.googlesyndication.com/simgad/5440373213328895821",
                "size": "5xl",
                "aspectMode": "cover",
                "aspectRatio": "150:196",
                "gravity": "center",
                "flex": 1
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://media.istockphoto.com/id/1316193521/zh/向量/業務領導和遠見卓識帶領公司成功職業方向或工作成就理念聰明的商人船長控制方向盤掌舵與望遠鏡的視野.jpg?s=612x612&w=0&k=20&c=9pPpEM3qPrjysUu-VHC_JFw0ceQScS-vV2kt_VaGe_U=",
                    "aspectMode": "cover",
                    "size": "full"
                  }
                ],
                "cornerRadius": "100px",
                "width": "72px",
                "height": "72px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "contents": [
                      {
                        "type": "span",
                        "text": "陳佳萱 Angel",
                        "weight": "bold",
                        "color": "#000000"
                      },
                      {
                        "type": "span",
                        "text": "     "
                      },
                      {
                        "type": "span",
                        "text": "\n嘿疲YOLO乳【隊長】AKA【團隊掌舵手】負責接洽團隊大小事 主導會議流程以及團隊問題 是團隊裡最能信任的隊長"
                      }
                    ],
                    "size": "sm",
                    "wrap": True
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "#隊長#天生的領導者",
                        "size": "sm",
                        "color": "#bcbcbc"
                      }
                    ],
                    "spacing": "sm",
                    "margin": "md"
                  }
                ]
              }
            ],
            "spacing": "xl",
            "paddingAll": "20px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://tpc.googlesyndication.com/simgad/2432546891997535283",
                "size": "5xl",
                "aspectMode": "cover",
                "aspectRatio": "150:196",
                "gravity": "center",
                "flex": 1
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://thumbs.dreamstime.com/b/企业人指挥隐喻领导力引领企业向成功经理引导和控制团队概念-239954077.jpg",
                    "aspectMode": "cover",
                    "size": "full"
                  }
                ],
                "cornerRadius": "100px",
                "width": "72px",
                "height": "72px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "contents": [
                      {
                        "type": "span",
                        "text": "李品澤 Jerry",
                        "weight": "bold",
                        "color": "#000000"
                      },
                      {
                        "type": "span",
                        "text": "     "
                      },
                      {
                        "type": "span",
                        "text": "\n嘿疲YOLO乳【副隊長】AKA【團隊鼓勵康樂擔當】負責處理團隊Coding以及提醒團員事情代辦事項 是團隊裡唯一的男性"
                      }
                    ],
                    "size": "sm",
                    "wrap": True
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "#副隊長#天生的啦啦隊",
                        "size": "sm",
                        "color": "#bcbcbc"
                      }
                    ],
                    "spacing": "sm",
                    "margin": "md"
                  }
                ]
              }
            ],
            "spacing": "xl",
            "paddingAll": "20px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://tpc.googlesyndication.com/simgad/12322700720950660648",
                "size": "5xl",
                "aspectMode": "cover",
                "aspectRatio": "150:196",
                "gravity": "center",
                "flex": 1
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://cdn-icons-png.flaticon.com/512/2631/2631384.png",
                    "aspectMode": "cover",
                    "size": "full"
                  }
                ],
                "cornerRadius": "100px",
                "width": "72px",
                "height": "72px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "contents": [
                      {
                        "type": "span",
                        "text": "Vera",
                        "weight": "bold",
                        "color": "#000000"
                      },
                      {
                        "type": "span",
                        "text": "     "
                      },
                      {
                        "type": "span",
                        "text": "\n嘿疲YOLO乳【商業顧問】AKA【團隊商學大腦】負責查詢以及調研商模融資相關資訊 主導成本預估模型製作 是團隊裡最強的馬來西亞人"
                      }
                    ],
                    "size": "sm",
                    "wrap": True
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "#商業天才#天生商業顧問",
                        "size": "sm",
                        "color": "#bcbcbc"
                      }
                    ],
                    "spacing": "sm",
                    "margin": "md"
                  }
                ]
              }
            ],
            "spacing": "xl",
            "paddingAll": "20px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://tpc.googlesyndication.com/simgad/11511305431362462344",
                "size": "5xl",
                "aspectMode": "cover",
                "aspectRatio": "150:196",
                "gravity": "center",
                "flex": 1
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://tpc.googlesyndication.com/simgad/11511305431362462344",
                    "aspectMode": "cover",
                    "size": "full"
                  }
                ],
                "cornerRadius": "100px",
                "width": "72px",
                "height": "72px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "contents": [
                      {
                        "type": "span",
                        "text": "張育華",
                        "weight": "bold",
                        "color": "#000000"
                      },
                      {
                        "type": "span",
                        "text": "     "
                      },
                      {
                        "type": "span",
                        "text": "\n嘿疲YOLO乳【現實顧問】AKA【團隊最強打工仔】負責提出關鍵性問題 每次都能一個問題點醒團員 主導會議結尾的提問 是團隊裡社會經驗最多的人"
                      }
                    ],
                    "size": "sm",
                    "wrap": True
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "#人脈#天生的提問家",
                        "size": "sm",
                        "color": "#bcbcbc"
                      }
                    ],
                    "spacing": "sm",
                    "margin": "md"
                  }
                ]
              }
            ],
            "spacing": "xl",
            "paddingAll": "20px"
          }
        ],
        "paddingAll": "0px"
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "image",
                "url": "https://tpc.googlesyndication.com/pimgad/15437272802181942983",
                "size": "5xl",
                "aspectMode": "cover",
                "aspectRatio": "150:196",
                "gravity": "center",
                "flex": 1
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "aspectMode": "cover",
                    "size": "full",
                    "url": "https://media.istockphoto.com/id/1265730983/zh/向量/女藝術家站在畫架附近-在白色背景上畫抽象形狀.jpg?s=612x612&w=0&k=20&c=3tdi1fWIXOOY_upR9jh6ZKSTbIZ9owV_P3fRS-6DSoY="
                  }
                ],
                "cornerRadius": "100px",
                "width": "72px",
                "height": "72px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "contents": [
                      {
                        "type": "span",
                        "text": "廖淨彤",
                        "weight": "bold",
                        "color": "#000000"
                      },
                      {
                        "type": "span",
                        "text": "     "
                      },
                      {
                        "type": "span",
                        "text": "\n嘿疲YOLO乳【藝術家】AKA【團隊美術設集總監】負責團隊各種Logo、海報、ppt、小手冊設計 主導任何美觀問題 是團隊裡美感天花板"
                      }
                    ],
                    "size": "sm",
                    "wrap": True
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": "#藝術總監#天生的藝術家",
                        "size": "sm",
                        "color": "#bcbcbc"
                      }
                    ],
                    "spacing": "sm",
                    "margin": "md"
                  }
                ]
              }
            ],
            "spacing": "xl",
            "paddingAll": "20px"
          }
        ],
        "paddingAll": "0px"
      }
    }
  ]
}
        )
            line_bot_api.reply_message(event.reply_token, flex_message)
        # if re.match(msg,"馬上水一波"):
        #     reply=client_data.confirm_client()
        #     line_bot_api.reply_message(event.reply_token,reply)
        # elif Status=="register_1":
        #     client_data.insert_clienet_data(user_id,msg)
        #     reply=client_data.confirm_client_name(msg)
        #     line_bot_api.reply_message(event.reply_token,reply)
        # elif Status=="register_2":
        #     client_data.update_client_data_phone(user_id,msg)
        #     reply=client_data.confirm_client_phone(msg)
        #    line_bot_api.reply_message(event.reply_token,reply)
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


    if 'action=一段話描述續水?' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 \n給【無法與台積電競爭水源】\n的【半導體用水大戶】\n我們提供【低成本且永續】\n的【雨水資源】\n相較其他\n【海水淡化廠與再生水廠】\n我們\n【單位造水與環境成本較低】\n因為\n【設備安裝成本較低且簡易也更節能】 \n💧"))
    elif 'action=法規是否確認過可行?' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 \n•水利法規範地面水和地下水為國有\n但雨水不算法規上可行無問題\n•已向環境法律人協會\n與前水利署員工等人脈諮詢過\n💧"))
    elif 'action=屋頂改建這部分合法嗎?' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 \n•有!是可行的\n但有建設尺寸的相關規範。\n•天溝不得突出建築物屋頂女兒牆外緣。\n💧"))
    elif 'action=何謂女兒牆' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/simgad/3786464081103359111',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)
    if 'action=極端氣候少雨頻率增加' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 2031年預估全國供水缺口\n可能會達到每日116萬噸 💧"))
    elif 'action=工業大戶急迫用水需求' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 台積電一天用水量為例\n竹科 🟥🟥🟥5.7噸\n中科 🟪🟪5.4噸\n南科 🟦🟦🟦🟦🟦8.2噸 💧"))
    elif 'action=半導體產業一缺水問題' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 2021年中科園區\n一噸水價飆升至$1000📈\n台積電每月斥資2億💸\n月包水車服務 💧"))
    elif 'action=新法規徵收耗水費' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 單月用水量\n超過😱9000噸的用水大戶\n每度徵收3元耗水費\n若開發水資源或\n投資節水設備者\n亦享有最高💰60%之耗水費減徵 💧"))
    elif 'action=相對成本' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/pimgad/18288553953039673224',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)
    
    if 'action=團隊匹配度' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 ①交大環工所指導研究台灣大型半導體代工廠商對於缺水困境的解方與用水數據\n②2022臺帛氣候變遷青年論壇工業用水主題主講人\n③掌握環境科學、法律與大型\n半導體代工廠商之關鍵人脈 💧"))
    elif 'action=不完全競爭市場' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 因成本過高\n目前多為政府部門推行\n尚無企業投入建設 💧"))
    elif 'action=商業模式可行性' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 延自太陽能售電業\n而TA清楚且資本雄厚 💧"))

    if 'action=雨水貯留系統' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 建築物屋頂作為系統的\n雨水收集範圍\n其集水面積的大小亦將決定\n可收集雨水量的多寡\n進而影響貯水設施設計的尺寸 💧"))
    elif 'action=雨水統流程圖' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/pimgad/6822892308033805966',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif 'action=雨水装置設計模型?' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/pimgad/1717383778888643550',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)
    
    if 'action=商業模式流程圖' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/simgad/3780474394281694695',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif 'action=為什麼願意參與續水的計畫?' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 『政府部門』可以收水權費\n『住戶』獲得被動收入且缺水時能優先取得水源\n『大樓、公寓、停車場』訂單回饋\n『用水大戶』獲得額外水資源且能減少耗水費繳納\n『銀行』可以收取高利息 💧"))
    elif 'action=我們的資金從哪裡來?' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 •天使投資人\n• 銀行融資\n•創投公會\n•和政府合作 💧"))
    
    
    
    if 'action=市場分析🆂分析' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/pimgad/1854290020990939253',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif 'action=市場分析🆆分析' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/pimgad/6465412230507175240',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif 'action=市場分析🅾分析' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/pimgad/3056922080588038835',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif 'action=市場分析🆃分析' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/pimgad/17883294396301247594',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif 'action=市場分析🆂🆆🅾🆃分析' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/pimgad/13894863598165272665',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)


    if 'action=如果可行 費用怎麼算?' in event.postback.data:
        reply=visitor.Budget_4()
        line_bot_api.reply_message(event.reply_token,reply)
    elif 'action=基本配備成本' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 管線\n(根據個別建築物高度做測量)\nPVC-A管:\n新台幣455元(4m)\nPVC-B厚管:\n新台幣1110元(5m) 💧"))
    elif 'action=水塔' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 (三公噸基於三月基隆平均雨量)\n塑膠:\n新台幣10,000一20,000元\n不鏽鋼:\n新台幣30,000-50,000元 💧"))
    elif 'action=初級淨水器加上濾水器' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 \n新台幣10000-30000元 💧"))
    elif 'action=未來規劃' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 \n由於我們沒辦法掌握市場需求的數據\n因此目前沒辦法計算出費用\n但在末來的活動中\n我們會繼續往這個方向做調研 💧"))


    if 'action=為什麼目前沒有人做這個?' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 \n•團隊成員深入了解\n太陽能售電業的商業模式\n完成半導體用水需求的專題研究\n我們將此商業模式應用於缺水痛點。\n\n•半導體用水大戶旁都有再生水廠\n而由2020起\n半導體產業強烈意識到水資源的不足\n因此痛點有『絕對的前瞻性』 💧"))
    elif 'action=怎麼解決靠天吃飯的問題?' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 \n•化危機為轉機:\n避免旱季儲水以降低儲水\n建設與維修成本\n並減少輿論抨擊\n形成正面企業形象\n•旱季時可以進行維護整修工程 💧"))
    elif 'action=如何收集水?' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 •水車就像垃圾車一樣\n到固定範圍區域做雨水收集 💧"))
    elif 'action=場地問題' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 \n•各廠商本來就有自家的儲水地\n我們將和廠商簽訂合約\n再用自家開發的APP\n與周邊住戶合作的儲水槽\n檢測雨水量\n存好水會直接載去廠商蓄水池 💧"))
    elif 'action=改建屋頂接管線是外包嗎？' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 這部分未來會再做研調\n待客群範圍更具體\n會再做估計與成本考量\n由於我們沒有這個技術層面\n所以屋頂接管線會找外包幫忙改 💧"))
    elif 'action=水管明渠是埋在地底下嗎？' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 明渠\n泛指任何用於排水的露天水道\n包括各種河道、運河、大型溝渠等 💧"))
    elif 'action=你們目標客群是誰？' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 無法與台積電競爭水資源的半導體用水大戶 💧"))
    elif 'action=大眾有意願嗎？' in event.postback.data:
        line_bot_api.reply_message(event.reply_token,TextSendMessage("💧 大多數住戶都喜歡被動收入\n例如:\n太陽能售電業——陽光伏特加為例\n陽光伏特加已有19632的體驗客戶\n但我們考慮初期部分不太能接受改變的用戶\n因此我們將與了解或能接受\n太陽能售電業的住戶合作\n建立信用，並打開曝光度。💧"))

    if 'action=市場分析🆂分析' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/simgad/8791108576365732220',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif 'action=市場分析🆆分析' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/pimgad/6465412230507175240',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif 'action=市場分析🅾分析' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/pimgad/3056922080588038835',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif 'action=市場分析🆃分析' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/pimgad/17883294396301247594',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)
    elif 'action=市場分析🆂🆆🅾🆃分析' in event.postback.data:
        image_message=ImageSendMessage(original_content_url='https://tpc.googlesyndication.com/pimgad/13894863598165272665',
                                       preview_image_url='https://thumb.photo-ac.com/57/5769ca1eb8b703800481e42a5942d08a_t.jpeg')
        line_bot_api.reply_message(event.reply_token,image_message)



    # if 'action=buy&itemid=1' in event.postback.data and Status=="register_4":          
    #     datetime_str = event.postback.params['datetime']
    #     datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M')
    #     reply_text = f'{datetime_obj.month}月{datetime_obj.day}日{datetime_obj.hour}點{datetime_obj.minute}分'
    #     client_data.update_client_data_install_date(user_id,reply_text)
    #     reply=client_data.confirm_client_install_date(reply_text)
    #     line_bot_api.reply_message(event.reply_token,reply)
    # elif 'action=Yes'  in event.postback.data and Status=="Standard":
    #     dbprofile.update_Status(user_id,"register_1")
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage("請輸入您的名字(全名):"))
    # elif 'action=No'  in event.postback.data and Status=="Standard":
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage("謝謝你～🥹"))
    # elif 'action=register_2'  in event.postback.data and Status=="register_1":
    #     dbprofile.update_Status(user_id,"register_2")
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage("請輸入您的電話號碼\n(格式為09XX XXX XXX)\n可以不用空格"))
    # elif 'action=wrong_1'  in event.postback.data and Status=="register_1":
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage("請輸入您的名字(全名):"))
    # elif 'action=register_3'  in event.postback.data and Status=="register_2":
    #     dbprofile.update_Status(user_id,"register_3")
    #     reply=client_data.select_address()
    #     line_bot_api.reply_message(event.reply_token,reply)
    # elif 'action=wrong_2'  in event.postback.data and Status=="register_2":
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage("請輸入您的電話號碼\n(格式為09XX XXX XXX)\n可以不用空格"))
    # elif 'action=register_4'  in event.postback.data and Status=="register_3":
    #     dbprofile.update_Status(user_id,"register_4")
    #     reply=client_data.select_date()
    #     line_bot_api.reply_message(event.reply_token,reply)
    # elif 'action=wrong_3'  in event.postback.data and Status=="register_3":
    #     reply=client_data.select_address()
    #     line_bot_api.reply_message(event.reply_token,reply)
    # elif 'action=register_5'  in event.postback.data and Status=="register_4":
    #     dbprofile.update_Status(user_id,"register_5")
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage("已幫你初始化一個儲水器～～～💦💦💦"))
    #     pass#開始模擬
    # elif 'action=wrong_4' in event.postback.data and Status=="register_4":
    #     reply=client_data.select_date()
    #     line_bot_api.reply_message(event.reply_token,reply)
    
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)