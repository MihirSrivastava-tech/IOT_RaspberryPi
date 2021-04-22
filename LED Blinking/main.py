from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

#Setting pin number 40 as output pin
GPIO.setup(40, GPIO.OUT)


while(True):
    #Giving pin number 40 value as high
    GPIO.output(40, GPIO.HIGH)
    sleep(0.5)
    #Giving pin number 40 value as low
    GPIO.output(40, GPIO.LOW)
    sleep(0.5)