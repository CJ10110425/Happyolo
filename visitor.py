import dbprofile
from linebot.models import *
import re


def introduce():    
    carousel_template_message = TemplateSendMessage(
                alt_text='pass',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url='https://tpc.googlesyndication.com/simgad/11326736544206713066',
                            title='續水',
                            text='———解答之書',
                            actions=[
                                MessageAction(
                                    label='瞭解更多',
                                    text='為我解答'
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
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://tpc.googlesyndication.com/pimgad/1039909767127289977',
                            title='團隊成員介紹',
                            text='———創業從來都不是一個人的事',
                            actions=[
                                MessageAction(
                                    label='想看看',
                                    text='YOLO'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://tpc.googlesyndication.com/pimgad/7943076260647570094',
                            title='相關照片',
                            text='———奮鬥的照片💪🏻💪🏻💪🏻',
                            actions=[
                                MessageAction(
                                    label='想看看',
                                    text='給我看看'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://tpc.googlesyndication.com/simgad/15065693788016217573',
                            title='隊呼！',
                            text='———開心做事、開心玩',
                            actions=[
                                MessageAction(
                                    label='想看看',
                                    text='Happy'
                                )
                            ]
                        )
                    ]
                )
            )
    return carousel_template_message

def subject_4():    
    carousel_template_message = TemplateSendMessage(
                alt_text='六大題',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url='https://png.pngtree.com/png-clipart/20220614/original/pngtree-people-seminar-icon-outline-vector-png-image_8014323.png',
                            title='簡介',
                            text='———嘿疲YOLO乳',
                            actions=[
                                MessageAction(
                                    label='瞭解更多',
                                    text='瞭解更多簡介'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://thumbs.dreamstime.com/z/学习、研究和检查问题-—-图为放大镜放大字题，象征着研究、探索和-164571350.jpg',
                            title='選題',
                            text='———嘿疲YOLO乳',
                            actions=[
                                MessageAction(
                                    label='瞭解更多',
                                    text='瞭解更多選題'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://elasticbeanstalk-ap-northeast-1-85031349581-ohbot-official-prod.s3.ap-northeast-1.amazonaws.com/image3_a2fea62a06.jpg',
                            title='市場 & 優勢',
                            text='———嘿疲YOLO乳',
                            actions=[
                                MessageAction(
                                    label='瞭解更多',
                                    text='瞭解更多市場 & 優勢'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://png.pngtree.com/png-clipart/20190831/ourlarge/pngtree-cartoon-hand-drawn-gears-operation-line-drawing-teamwork-illustration-png-image_1716821.jpg',
                            title='運作模式',
                            text='———嘿疲YOLO乳',
                            actions=[
                                MessageAction(
                                    label='瞭解更多',
                                    text='瞭解更多運作模式'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://png.pngtree.com/png-clipart/20220601/original/pngtree-business-models-word-concepts-banner-png-image_7840618.png',
                            title='商業模式',
                            text='———嘿疲YOLO乳',
                            actions=[
                                MessageAction(
                                    label='瞭解更多',
                                    text='瞭解更多商業模式'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://yunjoy.tw/images/study/marketing/mm10-SEGMENTATION.jpeg',
                            title='市場區隔',
                            text='———嘿疲YOLO乳',
                            actions=[
                                MessageAction(
                                    label='瞭解更多',
                                    text='瞭解更多市場區隔'
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url='https://www.hwataibank.com.tw/wp-content/uploads/2018/11/deposit-icon-1-1.jpg',
                            title='精打細算',
                            text='———嘿疲YOLO乳',
                            actions=[
                                MessageAction(
                                    label='瞭解更多',
                                    text='瞭解更多預算部分'
                                )
                            ]
                        ),  
                        CarouselColumn(
                            thumbnail_image_url='https://media.istockphoto.com/id/1073505842/cs/vektor/ikona-odpovědi-na-otázku-symbol-otázky-a-odpovědi.jpg?s=170667a&w=0&k=20&c=-v1VpNepqGoE-YMXNDaLLVXuZB922IPffs0-ie_AvF4=',
                            title='重點問題',
                            text='———嘿疲YOLO乳',
                            actions=[
                                MessageAction(
                                    label='瞭解更多',
                                    text='瞭解更多重點問題'
                                )
                            ]
                        )
                    ]
                )
            )
    return carousel_template_message

def introduction():
    image_carousel_template_message = TemplateSendMessage(
            alt_text='簡介',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️一段話描述續水?',
                            display_text='我想看這個',
                            data='action=一段話描述續水?'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️工法規是否確認過可行?',
                            display_text='我想看這個',
                            data='action=法規是否確認過可行?'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️屋頂改建這部分合法嗎?',
                            display_text='我想看這個',
                            data='action=屋頂改建這部分合法嗎?'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️何謂女兒牆',
                            display_text='我想看這個',
                            data='action=何謂女兒牆'
                        )
                    )
                ]
            )
        )
    return image_carousel_template_message





def chose_topic():
    image_carousel_template_message = TemplateSendMessage(
            alt_text='選題',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️極端氣候少雨頻率增加',
                            display_text='我想看這個',
                            data='action=極端氣候少雨頻率增加'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️工業大戶急迫用水需求',
                            display_text='我想看這個',
                            data='action=工業大戶急迫用水需求'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️半導體產業一缺水問題',
                            display_text='我想看這個',
                            data='action=半導體產業一缺水問題'
                        )
                    ),ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️新法規徵收耗水費',
                            display_text='我想看這個',
                            data='action=新法規徵收耗水費'
                        )
                    ),ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️相對成本',
                            display_text='我想看這個',
                            data='action=相對成本'
                        )
                    ),
                ]
            )
        )
    return image_carousel_template_message

def market_advantage():
    image_carousel_template_message = TemplateSendMessage(
            alt_text='市場 & 優勢',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️團隊匹配度',
                            display_text='我想看這個',
                            data='action=團隊匹配度'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️不完全競爭市場',
                            display_text='我想看這個',
                            data='action=不完全競爭市場'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️商業模式可行性',
                            display_text='我想看這個',
                            data='action=商業模式可行性'
                        )
                    )
                ]
            )
        )
    return image_carousel_template_message


def market_operation():
    image_carousel_template_message = TemplateSendMessage(
            alt_text='運作模式',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️雨水貯留系統',
                            display_text='我想看這個',
                            data='action=雨水貯留系統'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️雨水貯留系統流程圖',
                            display_text='我想看這個',
                            data='action=雨水統流程圖'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️雨水装置設計模型?',
                            display_text='我想看這個',
                            data='action=雨水装置設計模型?'
                        )
                    ),
                ]
            )
        )
    return image_carousel_template_message

def business_model():
    image_carousel_template_message = TemplateSendMessage(
            alt_text='商業模式',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️為什願意參與續水計畫?',
                            display_text='我想看這個',
                            data='action=為什麼願意參與續水的計畫?'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️我們的資金從哪裡來?',
                            display_text='我想看這個',
                            data='action=我們的資金從哪裡來?'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️商業模式流程圖',
                            display_text='我想看這個',
                            data='action=商業模式流程圖'
                        )
                    )
                ]
            )
        )
    return image_carousel_template_message

def market_segment():
    image_carousel_template_message = TemplateSendMessage(
            alt_text='市場區隔',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13934656067111684668',
                        action=PostbackAction(
                            label='♨️市場分析🆂分析',
                            display_text='我想看這個',
                            data='action=市場分析🆂分析'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/pimgad/7131958582562101640',
                        action=PostbackAction(
                            label='♨️市場分析🆆分析',
                            display_text='我想看這個',
                            data='action=市場分析🆆分析'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/10934323776665448559',
                        action=PostbackAction(
                            label='♨️市場分析🅾分析',
                            display_text='我想看這個',
                            data='action=市場分析🅾分析'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/pimgad/548199028666392788',
                        action=PostbackAction(
                            label='♨️市場分析🆃分析',
                            display_text='我想看這個',
                            data='action=市場分析🆃分析'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/pimgad/4718524794212657073',
                        action=PostbackAction(
                            label='♨️市場分析🆂🆆🅾🆃分析',
                            display_text='我想看這個',
                            data='action=市場分析🆂🆆🅾🆃分析'
                        )
                    )
                ]
            )
        )
    return image_carousel_template_message


def Budget():
    image_carousel_template_message = TemplateSendMessage(
            alt_text='預算',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️如果可行 費用怎麼算?',
                            display_text='我想看這個',
                            data='action=如果可行 費用怎麼算?'
                        )
                    )
                ]
            )
        )
    return image_carousel_template_message


def Budget_4():
    image_carousel_template_message = TemplateSendMessage(
            alt_text='預算',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️基本配備成本',
                            display_text='我想看這個',
                            data='action=基本配備成本'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️水塔',
                            display_text='我想看這個',
                            data='action=水塔'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨初級淨水器加上濾水器',
                            display_text='我想看這個',
                            data='action=初級淨水器加上濾水器'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️未來規劃',
                            display_text='我想看這個',
                            data='action=未來規劃'
                        )
                    )
                ]
            )
        )
    return image_carousel_template_message

def important_que():
    image_carousel_template_message = TemplateSendMessage(
            alt_text='重點整理',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️為什麼沒有人做這個?',
                            display_text='我想看這個',
                            data='action=為什麼目前沒有人做這個?'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️怎麼解決靠天吃飯問題?',
                            display_text='我想看這個',
                            data='action=怎麼解決靠天吃飯的問題?'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨如何收集水?',
                            display_text='我想看這個',
                            data='action=如何收集水?'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️場地問題',
                            display_text='我想看這個',
                            data='action=場地問題'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️改建屋頂管線是外包嗎？',
                            display_text='我想看這個',
                            data='action=改建屋頂接管線是外包嗎？'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️水管明渠是埋地底下嗎？',
                            display_text='我想看這個',
                            data='action=水管明渠是埋在地底下嗎？'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️你們目標客群是誰？',
                            display_text='我想看這個',
                            data='action=你們目標客群是誰？'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://tpc.googlesyndication.com/simgad/13203120254957692772',
                        action=PostbackAction(
                            label='♨️大眾有意願嗎？',
                            display_text='我想看這個',
                            data='action=大眾有意願嗎？'
                        )
                    )
                ]
            )
        )
    return image_carousel_template_message
