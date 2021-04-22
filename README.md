# IOT_RaspberryPi

## Examples for using Raspberry Pi in IOT with various Input and Output devices 

### What is Raspberry Pi
It is a small single board computer that can be used for learning, programming and for developing projects based on IOT or embedded systems.

### Basics of GPIO Programming on Raspberry Pi
- To import the Raspberry Pi module use `from RPi import GPIO`
- To set the mode to BOARD numbering system use `GPIO.setmode(GPIO.BOARD)`
- To make the pin as input pin, use `GPIO.setup(PIN_NUMBER, GPIO.IN)`
- To make the pin as output pin, use `GPIO.setup(PIN_NUMBER,GPIO.OUT)`
- To take input from the pin, use `GPIO.input(PIN_NUMBER)`
  > When the input is given, the value returned by the function will be 1 else it will be 0
- To give output to the pin, use `GPIO.output(PIN_NUMBER, OUTPUT_VALUE)`
  > * To make the value high, use `GPIO.HIGH` in place of `OUTPUT_VALUE`
  > * To make the value low, use `GPIO.LOW` in place of `OUTPUT_VALUE` 
- **Note:-** Change the `PIN_NUMBER` to the required pin number value


  
        

