import re
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('5qZK8DqEFEYoJuw9Iaar5xUNMHldHV4mFayB2OZeWGqMMeKYf+rMrH7F0BsdanQrZWTfqLlBYyj86RIBjgtkM5N7LifzdU7Bp2/GnwBVakNN35PxQRmNRW4u8oAbtg2i8Myr2UuB6rf/sN+CF267AgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('aeadbadcf92bf257a23cd04fdfb2365d')

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
#    message = TextSendMessage(text="歡迎來到STORY!")
    ll = ['http','https', '新竹','竹北','台北','美食','宜蘭','台中','桃園','新北','基隆','抽','.com','.tw','test']
    if any(s in message.text for s in ll)==False:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='嗶嗶！聊天犯規！\n格式為\n訊息一：\n地名＋美食形式\n訊息二：\n相關網址\n必填地名支援：\n新竹/竹北/台北/台中/新北\n正在開發將內容整理成雲端文件\n使用上問題請找odie'))
    if '抽' in message.text:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='抽什麼抽！'))

#    test1 = ImageSendMessage(original_content_url='http://cfruit.tw/wp-content/uploads/2018/07/area01_Red_White_Yellow_Red_Yellow_White.png',preview_image_url='http://cfruit.tw/wp-content/uploads/2018/07/area01_Red_White_Yellow_Red_Yellow_White.png')
    test1 = ImageSendMessage(original_content_url='https://drive.google.com/uc?id=1O2rhUO8z8jkjUABHpqLhD71-wwveiZrk',preview_image_url='https://drive.google.com/uc?id=1O2rhUO8z8jkjUABHpqLhD71-wwveiZrk')
    if 'test01' in message.text:
#        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='DEMO CASE 01'))
        line_bot_api.reply_message(event.reply_token,test1)

    test3 = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='Are you sure?',
            actions=[
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='message',
                    text='message text'
                )
            ]
        )
    )

    if 'test03' in message.text:
#        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='DEMO CASE 01'))
        line_bot_api.reply_message(event.reply_token,test3)

    test2 = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://example.com/image.jpg',
            title='Menu',
            text='Please select',
            actions=[
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='message',
                    text='message text'
                ),
                URITemplateAction(
                    label='uri',
                    uri='http://example.com/'
                )
            ]
        )
    )
#https://drive.google.com/open?id=1O2rhUO8z8jkjUABHpqLhD71-wwveiZrk
    if 'test02' in message.text:
#        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='DEMO CASE 01'))
        line_bot_api.reply_message(event.reply_token,test2)
#    else:
#        line_bot_api.reply_message(event.reply_token,message)
#    line_bot_api.reply_message(event.reply_token,message)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
