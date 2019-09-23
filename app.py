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
import urllib.request

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('qiQ6AitzlEll276qnvY10dJyNjwOXWAVHC2EIwwGP5KolImWIjgngAa/Fe6HfSOm6bnONl2Jn4D6CDoepmBNjrHY/lbt3qGC3tzukx5lXrJCCPDs2w7IymHCUvzHIKY7qv5sJrn8KjK3lyjd/BfMLwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('c107d467f524937d70442c5290550486')

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
#    ll = ['測站一','測站二','測站三']
#    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='Lets Go!'))
    if '使用說明' in message.text:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請輸入一號站、二號站或是三號站以擷取測站量測資料'))
    if '一號站' in message.text:
        loc1 = 'http://ec2-54-175-179-28.compute-1.amazonaws.com/get_line_bot_data.php?device_id=7504'
        response = urllib.request.urlopen(loc1)
        html = response.read()
        html = str(html)
        aa = re.split('<br>|b\'',html)
        aa1 = aa[1].replace(',',' ')
        ddl = re.split('=',aa1)
        ddtemp = re.split(' ',ddl[3])
        dd = ddtemp[1]
        if float(dd) < 0:
            dd = '0.0'
        tttemp = re.split(' ',ddl[2])
        ttq = tttemp[1]
        tt = ttq[0:12]
        wmgs = '介壽村道路淹水感知查詢資訊\n--------------------------------\n目前水位'+dd+'公分\n(地表高程起算以上)\n最後更新時間：'+tt
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=wmgs))
    if '二號站' in message.text:
        loc2 = 'http://ec2-54-175-179-28.compute-1.amazonaws.com/get_line_bot_data.php?device_id=7506'
        response = urllib.request.urlopen(loc2)
        html = response.read()
        html = str(html)
        aa = re.split('<br>|b\'',html)
        aa2 = aa[1].replace(',',' ')
        ddl2 = re.split('=',aa2)
        ddtemp2 = re.split(' ',ddl2[3])
        dd2 = ddtemp2[1]
        if float(dd2) < 0:
            dd2 = '0.0'
        tttemp2 = re.split(' ',ddl2[2])
        ttq2 = tttemp2[1]
        tt2 = ttq2[0:12]
        wmgs = '復興村道路淹水感知查詢資訊\n--------------------------------\n目前水位'+dd2+'公分\n(地表高程起算以上)\n最後更新時間：'+tt2
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=wmgs))
    if '三號站' in message.text:
        loc3 = 'http://ec2-54-175-179-28.compute-1.amazonaws.com/get_line_bot_data.php?device_id=7505'
        response = urllib.request.urlopen(loc3)
        html = response.read()
        html = str(html)
        aa = re.split('<br>|b\'',html)
        aa3 = aa[1].replace(',',' ')
        ddl3 = re.split('=',aa3)
        ddtemp3 = re.split(' ',ddl3[3])
        dd3 = ddtemp3[1]
        if float(dd3) < 0:
            dd3 = '0.0'
        tttemp3 = re.split(' ',ddl3[2])
        ttq3 = tttemp3[1]
        tt3 = ttq3[0:12]
        wmgs = '珠螺村道路淹水感知查詢資訊\n--------------------------------\n目前水位'+dd3+'公分\n(地表高程起算以上)\n最後更新時間：'+tt3
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=wmgs))
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
