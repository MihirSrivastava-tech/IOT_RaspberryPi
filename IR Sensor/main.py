from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

#Setting pin number 40 as output pin
GPIO.setup(40, GPIO.OUT)
#Setting pin number 5 as input pin
GPIO.setup(5, GPIO.IN)

count = 0

while(True):
    #Taking input from pin number 5, if input is being made the value return in GPIO.input() will be 1 else 0
    if GPIO.input(5):
      GPIO.output(40, GPIO.HIGH)
      count+=1
      print(count)
      while(GPIO.input(5)):
        continue
      GPIO.output(40, GPIO.LOW)
