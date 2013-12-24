import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # Use RPi pin numbers

PIN = 11 # Pin from Raspberry where the led will be connected
GPIO.setup(PIN, GPIO.OUT)

# Timings according to wikipedia:
# http://en.wikipedia.org/wiki/Morse_code#Representation.2C_timing_and_speeds

DIT = 0.2 # Duration of dit and pause between intra-character spacing
DAH = DIT * 3 # Duration of dah and pause between letters
PW = DIT * 7 # Pause between words

MORSE_CODE = {
    ' ' : ' ',
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
    '0' : '-----',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    ':' : '---...',
    ';' : '-.-.-.',
    '?' : '..--..',
    "'" : '.----.',
    '(' : '-.--.-',
    ')' : '-.--.-',
    ',' : '--..--',
    '-' : '-....-',
    '.' : '.-.-.-',
    '/' : '-..-.',
}

def validate(user_input):
    '''
    Function which will validate the user input.
    user_input: string, This will translated into morse code
    '''
    forbidden = []
    for char in user_input:
        if char.upper() not in MORSE_CODE.keys() and char != ' ':
            forbidden.append(char)

    forbidden_length = len(forbidden)

    if forbidden_length > 0:
        forbidden_letters = ', '.join(str(char) for char in forbidden)
        print "This characters cannot be translated into Morse Code: %s" % forbidden_letters
        return False
    else:
        return True

def dit():
    '''
    This function will turn on the LED when is a dih(.) for
    dih units of time then turn off the led and wait same dih units of time
    '''
    GPIO.output(PIN, True)
    time.sleep(DIT)
    GPIO.output(PIN, False)
    time.sleep(DIT)

def dah():
    '''
    This function will turn on the LED when is a dah(-) for
    dah units of time then turn off the led and wait dih units of time
    '''
    GPIO.output(PIN, True)
    time.sleep(DAH)
    GPIO.output(PIN, False)
    time.sleep(DIT)

cases = {
    '-' : dah,
    '.' : dit
}

def translate():
    while True:
        while True:
            user_input = raw_input('What would you like to say in Morse Code? :')
            if validate(user_input):
                break


        for letter in user_input:
            print letter
            time.sleep(DAH)
            for morse in MORSE_CODE[letter.upper()]:
                print morse
                time.sleep(PW) if morse == ' ' else cases[morse]()

if __name__ == '__main__':
    translate()
