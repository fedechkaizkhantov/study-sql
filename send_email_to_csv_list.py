# from smtplib import SMTP_SSL as SMTP
import smtplib
import mimetypes
import email
import email.mime.application
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

def send_mail():
    with open("email.csv", 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print (row[1]) #проверка что в столбце емайлы
#             формируем письмо
            msg = email.mime.multipart.MIMEMultipart()
            msg['Subject'] = 'Семинар'
            msg['From'] = 'login'
            msg['To'] = row[1]
            body = email.mime.text.MIMEText("""Здравствуйте, коллеги!""")
            msg.attach(body)
#            прикрепляем файлики 
            filename = 'сертификаты ' + row[0] + '.pdf'
            filename2 = '2.pdf'
            fp = open(filename,'rb')
            fp2 = open(filename2,'rb')
            att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
            att2 = email.mime.application.MIMEApplication(fp2.read(),_subtype="pdf")
            fp.close()
            fp2.close()
            att.add_header('Content-Disposition','attachment',filename=filename)
            att2.add_header('Content-Disposition','attachment',filename='2.pdf')
            msg.attach(att)
            msg.attach(att2)
#             используем smtp (проблема яндекса не решена, отказ в доступе)
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login('login','password')
            s.sendmail('login',row[1], msg.as_string())
            s.quit()
send_mail()  
