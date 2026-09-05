import smtplib
from random import randint
import os
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime


load_dotenv()
sender = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')
page = randint(1,3)

dates = datetime.now().month,datetime.now().day
df = pd.read_csv('birthdays.csv')
birthday_day = {(row['month'],row['day']):row for (index,row) in df.iterrows()}

if dates in birthday_day:
    details = birthday_day[dates]
    file_paths = f"letter_templates/letter_{page}.txt"
    with open(file_paths,'r') as f:
        massage = f.read().replace('[NAME]','Pawan').replace('Angela','NAGAR')
    with smtplib.SMTP('smtp.gmail.com',587) as server:
        server.starttls()
        server.login(sender,password=password)
        server.sendmail(from_addr=sender,to_addrs=details['email'],msg=f"Subject:Happy birthday,{massage}")

