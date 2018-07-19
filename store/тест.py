import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
from dateutil.relativedelta import relativedelta


def sendEMail():
    server = smtplib.SMTP()
    server.connect("smtp.gmail.com", 587)
    server.starttls()
    server.login("funnymanalex25@gmail.com", "3141592653589793AAATripple")

    server.sendmail("funnymanalex25@gmail.com", "permenev.alex@ya.ru", multi_msg.as_string())
    server.quit()


sendEMail()
# print(relativedelta(datetime(1, 1, 1, 23, 0, 0), datetime(1, 1, 1, 22, 55, 0)).minutes)
