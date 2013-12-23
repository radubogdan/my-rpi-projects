import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # Use RPi pin numbers

pins = [11, 12, 13, 15] # Pin list

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

def _reset():
    '''
    This function will turn of all leds
    '''
    for pin in pins:
        GPIO.output(pin, False)

def fwChase(frq):
    '''
    frq: float, number in miliseconds for sleep
    This function will fire up all leds from the first one
    in pins list to the last one with a given frequency
    '''
    for pin in pins:
        GPIO.output(pin, True)
        time.sleep(frq)
    for pin in pins:
        GPIO.output(pin, False)
        time.sleep(frq)
    for pin in reversed(pins):
        GPIO.output(pin, True)
        time.sleep(frq)
    for pin in reversed(pins):
        GPIO.output(pin, False)
        time.sleep(frq)


user_input = raw_input("What is the frequency?")
while True:
    _reset()
    fwChase(float(user_input))
