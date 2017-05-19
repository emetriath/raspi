# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)

pinA = 23
pinB = 22

#check
print("#### CHECK ####")
print("Connect raspi 5v")
print("Connect raspi GPIO:"+ str(pinA) + " to IN A")
print("Connect raspi GPIO:"+ str(pinB) + " to IN B")
print("Connect Pin8 Vs2 B High for work")
print("###############")

# IN_A
GPIO.setup(pinA, GPIO.OUT)
# IN_B
GPIO.setup(pinB, GPIO.OUT)

BASESTEPANGLE = 1.8;

speed = 0.02

angle = 180
ran = int(angle/BASESTEPANGLE/4)

try:
    for num in range(0,ran):
        GPIO.output(pinA,1)
        GPIO.output(pinB,1)
        sleep(speed)

        GPIO.output(pinA,0)
        GPIO.output(pinB,1)
        sleep(speed)

        GPIO.output(pinA,0)
        GPIO.output(pinB,0)
        sleep(speed)

        GPIO.output(pinA,1)
        GPIO.output(pinB,0)
        sleep(speed)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
