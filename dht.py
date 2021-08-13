import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import urllib2

DHTpin = 26

key="9GYZHZPENLKJK92N"
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)     

def readDHT():
    humi, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)
    return (str(int(humi)), str(int(temp)))

def main():
    
    print 'System Ready...'
    URL = 'https://api.thingspeak.com/update?api_key=%s' % key
    print "Wait...."
    while True:
            (humi, temp)= readDHT()
            finalURL = URL +"&field1=%s&field2=%s"%(humi, temp) 
            print finalURL
            s=urllib2.urlopen(finalURL);
            print humi+ " " + temp + " "
            s.close()
            time.sleep(10)
     
if __name__=="__main__":
   main()