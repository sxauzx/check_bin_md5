#!/usr/bin/python
import os
import os.path
import hashlib
import sqlite3
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText

mail_host="smtp.qq.com"
mail_user="1033317866@qq.com"
mail_pass="kxvtommkcslrbdfg"

sender = '1033317866@qq.com'
receivers = ['zhangxiang@rytx.com']

dirpath=["/root/","/bin/","/boot/","/dev/","/etc/","/home/","/lib/","/lib64/","/srv/","/sys/","/usr/"]
urls=[]
for direct in dirpath:
    for parent,dirnames,filenames in os.walk(direct):
        for file_name in filenames:
            file_path=os.path.join(parent,file_name)
            urls.append(file_path)

#def file(pathdir):
#    all_pro = os.listdir(pathdir)
#    childgroup = []
#    for pro in all_pro:
#        child = os.path.join('%s%s' % (pathdir, pro))
#        childgroup.append(child)
#    return childgroup

def check(url):
    check_path = os.getcwd()
    diff_bin = []
    check=hashlib.md5()
    check.update(url)
    result = str.format(check.hexdigest())
    conn = sqlite3.connect('%s/bin.md5' % (check_path))
    cursor = conn.cursor()
    cursor.execute("select md5 from checksum where url='%s';" % (url))
    result_new = cursor.fetchall()
    try:
        new=result_new[0][0]
    except IndexError, e:
        new="null"
#        print result, new
    if result != new:
        diff_bin.append('%s %s' % (url, result))
    conn.commit()
    for item in diff_bin:
        print item
#    return diff_bin
    diff_str='\n'.join(diff_bin)
    return diff_str

def send_mail(check_list):
    mail_send='\n'.join(check_list) 
    message = MIMEText('%s' % (mail_send),'plain', 'utf-8')
    message['From'] = ('%s<%s>') % (Header('1033317866@qq.com','utf-8'),'1033317866@qq.com')
    message['To'] = ('%s<%s>') % (Header("zhangxiang@rytx.com", 'utf-8'), 'zhangxiang@rytx.com')

    subject = "server check"
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
#        print "email send success"
    except smtplib.SMTPException,e:
        print e

    
if __name__=='__main__':
    check_list=[]
    for url in urls:
        send_check=check(url)
        check_list.append(send_check)
    send_mail(check_list)

