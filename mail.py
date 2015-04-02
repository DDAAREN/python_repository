#!/bin/usr/env python
#!_*_ coding:UTF-8 _*_

__author__ = 'pt'

"""
    发送邮件模板
"""

import smtplib
from email.mime.text import MIMEText



mailto_list = ['787351047@qq.com']
mail_host = "smtp.163.com"
mail_user = "ddaaren@163.com"
mail_pass = ""
mail_postfix = "163.com"


def send_mail(to_list, sub, content):
        me = "<"+mail_user+">"
        msg = MIMEText(content, _subtype='html', _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
                server = smtplib.SMTP()
                server.connect(mail_host)
                server.login(mail_user, mail_pass)
                server.sendmail(me, to_list, msg.as_string())
                server.close()
                return True
        except Exception, e:
                print str(e)
                return False

if __name__ == '__main__':
    if send_mail(mailto_list, "hello", "hello world！"):
        print "发送成功"
    else:
        print "发送失败"

"""
_subtype='' 字段决定发送的邮件内容类型：
    plain：普通文本
    html：html页面
"""