"""
@Time:2021/4/223:20
@Author:deanywang
@File:sendEmail.py
@return:""
"""
import  smtplib
from  email.mime.text import MIMEText

class sendmail:

    def  send_mail(self,path):
        f=open(path,'rb')
        mail_body=f.read()
        f.close()

        host="smtp.163.com"
        port=465
        sender='243688409@qq.com'
        pwd="sdkshdf" #��Щ���õ���Ȩ��
        receiver='243688409@qq.com'

        msg=MIMEText(mail_body,'HTML','UTF-8')
        msg['subject']="api���Ա��淢��"
        msg['from']=sender
        msg['to']=receiver


        s=smtplib.SMTP_SSL(host,port)
        s.login(sender,pwd)
        s.sendmail(sender,receiver,msg.as_string())
