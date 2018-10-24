#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import config

# 第三方 SMTP 服务
mail_host =  config.MAIL_HOST  # 设置服务器
mail_user = config.MAIL_USER  # 用户名
mail_pass = config.MAIL_PASS  # 口令

sender = config.SENDER_EMAIL
receivers = config.RECEIVER_EMAIL  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("314243", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")