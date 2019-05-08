#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dayan.common.get_newreport import get_report_file
from dayan.config import readcfg

def send_email_qq():
    #第三方 SMTP 服务
    mail_server = readcfg.smtp_server  # SMTP服务器smtp.qq.com
    mail_port = readcfg.port
    mail_sender = readcfg.sender  # 用户名390292699@qq.com
    mail_pass = readcfg.psw  # 密码nhpqsplzytrpbibe

    sender = readcfg.sender  # 发件人邮箱390292699@qq.com
    receivers = readcfg.receiver  # 接收人邮箱390292699@qq.com

    with open(get_report_file(),'rb') as f:
        mail_body=f.read()

    #定义邮件内容
    msg=MIMEMultipart()
    body=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['Subject']=u'自动化测试报告'
    msg['From']=sender
    msg['To']=receivers
    msg.attach(body)

    # 添加附件
    att=MIMEText(open(get_report_file(),'rb').read(),'base64',"utf-8")
    att['Content-Type']='application/octet-stream'
    att['Content-Disposition']="attachment;filename='report.html'"
    msg.attach(att)
    try:
        smtpObj = smtplib.SMTP_SSL(mail_server, mail_port)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_sender, mail_pass)  # 登录验证
        smtpObj.sendmail(mail_sender, receivers,msg.as_string())
        print("mail has been send successfully.")
    except smtplib.SMTPException as  e:
        print(e)
        raise


if __name__ == '__main__':
    send_email_qq()

