import RPi.GPIO as GPIO
from time import sleep

LED = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        sleep(1)
        GPIO.output(LED, GPIO.LOW)
        sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
