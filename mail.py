import smtplib
from email.mime.text import MIMEText


def sendmail(recver, state,content = 'by LiYang'):
    sender = "***@163.com"
    password = "***"
    if state == 1:
        message = MIMEText(content,"plain","utf-8")
        message['Subject'] = '打卡成功'
        message['To'] = recver
        message['From'] = sender
        smtp = smtplib.SMTP_SSL("smtp.163.com",994)
        smtp.login(sender,password)
        smtp.sendmail(sender,[recver],message.as_string())
        smtp.close()
    else:
        message = MIMEText(content, "plain", "utf-8")
        message['Subject'] = "打卡失败"
        message['To'] = recver
        message['From'] = sender
        smtp = smtplib.SMTP_SSL("smtp.163.com", 994)
        smtp.login(sender, password)
        smtp.sendmail(sender, [recver], message.as_string())
        smtp.close()

if __name__ == '__main__':
    sendmail('***@qq.com',1)