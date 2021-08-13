import RPi.GPIO as GPIO
import water
import datetime
from twilio.rest import Client
account_sid = 'ACea576c2fdc2c3939e2b80c9b68b1da53'
auth_token = 'f4996d8af5dde105a2212ed9be81adcd'
client = Client(account_sid, auth_token)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

if __name__ == "__main__":
    count=0
    status=water.get_status()
    while True:
        while status==1:
            if(count==0):
                message = client.messages.create(body="Motor Turned ON",from_='+13304089194',to='+919154860045')
                print('Motor on')
            status=water.get_status()
            water.init_output(40)
            GPIO.output(40, GPIO.LOW)
            f = open("last_watered.txt", "w")
            f.write("Last watered {}".format(datetime.datetime.now()))
            count=1
            f.close()
        
        while status==0:
            if(count==1):
                message = client.messages.create(body="Motor Turned Off",from_='+13304089194',to='+919154860045')
                print('motor off')
            status=water.get_status()
            GPIO.cleanup(40)
            count=0