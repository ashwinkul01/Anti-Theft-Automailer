import smtplib
from time import timezone
from tkinter import N
import requests
res = requests.get('https://ipinfo.io/')
data = res.json()

city = data['city']
region= data['region']
country= data['country']
loc= data['loc']
timezone=data['timezone']
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ashwincollegeproject@gmail.com','Ashwin@123')
    subject= 'ALERT: SUSPECT FOUND!!'
    body= 'Your most wanted criminal found at:\n'+'CITY: '+city +'\n REGION: '+region+'\n COUNTRY: '+country+'\n LOCATION: '+loc+'\n TIME ZONE: '+timezone
    msg=f'Subject: {subject}\n\n{body}'
    smtp.sendmail('ashwincollegeproject@gmail.com', 'ashwinkulshrestha01@gmail.com',msg)
    import requests

res = requests.get('https://ipinfo.io/')
data = res.json()

city = data['city']

location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]

print("Latitude : ", latitude)
print("Longitude : ", longitude)
print("City : ", city)