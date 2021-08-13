import RPi.GPIO as GPIO
import datetime
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def get_last_watered():
    try:
        f=open('last_watered.txt',"r")
        return f.readline()
        f.close()
    except:
        return "NEVER!"

def get_status(pin=8):
    GPIO.setup(pin ,GPIO.IN)
    return GPIO.input(pin)

def init_output(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)

def pump_on(pump_pin=40):
    init_output(pump_pin)
    f = open("last_watered.txt", "w")
    f.write("Last watered {}".format(datetime.datetime.now()))
    f.close()
    GPIO.output(pump_pin, GPIO.LOW)
    time.sleep(2)
    GPIO.cleanup(40)
    
def pump_off(pump_pin=40):
    init_output(pump_pin)
    GPIO.cleanup(40)
        
def get_rain(pin=38):
    GPIO.setup(pin ,GPIO.IN)
    return GPIO.input(pin)