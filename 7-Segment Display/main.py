from RPi import GPIO
from time import sleep


#           g   f   d   e   c   b   a
ssd_pins = [31, 33, 35, 37, 40, 38, 36]
# Based on common anode 7 segment display
digit = [[0,1,1,1,1,1,1], #0
         [0,0,0,0,1,1,0], #1
         [1,0,1,1,0,1,1], #2
         [1,0,0,1,1,1,1], #3
         [1,1,0,0,1,1,0], #4
         [1,1,0,1,1,0,1], #5
         [1,1,1,1,1,0,1], #6
         [0,0,0,0,1,1,1], #7
         [1,1,1,1,1,1,1], #8
         [1,1,0,1,1,1,1]  #9
        ]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ssd_pins, GPIO.OUT)
GPIO.setup(5, GPIO.IN)



i=0
while(True):
    if GPIO.input(5):
      i+=1
      if i==10:
        i=0
      GPIO.output(ssd_pins, digit[i])
      print(i)
      while GPIO.input(5):
        continue