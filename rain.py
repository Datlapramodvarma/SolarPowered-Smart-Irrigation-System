import RPi.GPIO as GPIO
import water
from twilio.rest import Client
account_sid = 'ACea576c2fdc2c3939e2b80c9b68b1da53'
auth_token = 'f4996d8af5dde105a2212ed9be81adcd'
client = Client(account_sid, auth_token)

rain_count=0

while True:
    rain=water.get_rain()
    if(rain==0 and rain_count==0):
        print 'Its Raining'
        message = client.messages.create(body="It's Raining",from_='+13304089194',to='+919154860045')
        rain_count=1
    if(rain==1 and rain_count==1):
        print 'Not Raining'
        rain_count=0