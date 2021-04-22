from RPi import GPIO

GPIO.setmode(GPIO.BOARD)

#Setting pin number 40 as output pin
GPIO.setup(40, GPIO.OUT)

#Giving pin number 40 value as high
GPIO.output(40, GPIO.HIGH)
