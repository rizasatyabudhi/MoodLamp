import RPi.GPIO as GPIO

redPin = 11  # Set to appropriate GPIO
greenPin = 15  # Should be set in the
bluePin = 13  # GPIO.BOARD format

def blink(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

#Base Color
def redOn():
    blink(redPin)
def greenOn():
    blink(greenPin)
def blueOn():
    blink(bluePin)

#Combination Color
def yellowOn():
    blink(redPin)
    blink(greenPin)

def cyanOn():
    blink(greenPin)
    blink(bluePin)

def magentaOn():
    blink(redPin)
    blink(bluePin)

def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)

#Turn lights off
def redOff():
    turnOff(redPin)

def greenOff():
    turnOff(greenOff)

def blueOff():
    turnOff(bluePin)

def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)

def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)

def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)

def reset():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)

