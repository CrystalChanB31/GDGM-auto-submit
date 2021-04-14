import requests
from datetime import datetime, timedelta, timezone
title_text = '[2601-1]自动填表结果'
class RlMessage:
    # 初始化类
    def __init__(self, username):
        self.username = username
    def sendMail(self, status, msg):
        res =requests.post(url='https://qmsg.zendee.cn/send/【qmsg酱KEY】',data={'msg': title_text + '\n当前用户：' + str(self.username) + "\n提交结果：" +str(msg)+ "\n时间："+ getTimeStr()})
def getTimeStr():
        utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
        bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
        return bj_dt.strftime("%Y年%m月%d日 %H:%M:%S")