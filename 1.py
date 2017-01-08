#!/usr/bin/ python2
#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
sender = '438090154@qq.com'
receiver = 'liaozhenhua@hust.edu.cn'
subject = 'python email test'
smtpserver = 'smtp.qq.com' 
username = '438090154@qq.com'
password = 'liao111'
  
msg = MIMEText('你好,python email test','text','utf-8')#中文需参数‘utf-8’，单字节字符不需要  
msg['Subject'] = Header(subject, 'utf-8')  
  
smtp = smtplib.SMTP()  
smtp.connect(smtpserver)
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
