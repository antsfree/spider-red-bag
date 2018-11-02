from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import time
import config
from user_info import get_user_list


def send_email(other_content='', errors='None'):
    """
    发邮件
    :return:
    """
    try:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime());
        # qq邮箱smtp服务器
        host_server = config.MAIL_HOST
        # sender_qq为发件人的qq号码
        sender_qq = config.MAIL_USER
        # pwd为qq邮箱的授权码
        pwd = config.MAIL_PASS
        # 发件人的邮箱
        sender_qq_mail = config.SENDER_EMAIL
        # 收件人邮箱
        receiver = config.RECEIVER_EMAIL
        # 邮件的正文内容
        user_list = str(get_user_list('user_name,user_money'))
        mail_content = f'{other_content} \n {user_list} \n Errors: {errors}'
        # 邮件标题
        mail_title = f'{current_time} 脚本处理结果报告'

        # ssl登录
        smtp = SMTP_SSL(host_server)
        # set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.set_debuglevel(1)
        smtp.ehlo(host_server)
        smtp.login(sender_qq, pwd)

        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_qq_mail
        msg["To"] = receiver
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        smtp.quit()
        return True
    except Exception:
        return False
