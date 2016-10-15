# -*- coding: utf-8 -*-
#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep

class Turret():

    PIN_A = 23
    PIN_B = 22
    POWER = 27

    BASE_STEP_ANGLE = 1.8;

    SPEED = 0.02

    def __init__(self):

        GPIO.setmode(GPIO.BCM)
        # IN_A
        GPIO.setup(self.PIN_A, GPIO.OUT)
        # IN_B
        GPIO.setup(self.PIN_B, GPIO.OUT)

        GPIO.setup(self.POWER, GPIO.OUT)

    def right(self, angle = 180):

        GPIO.output(self.POWER, GPIO.HIGH)
        ran = int(angle/self.BASE_STEP_ANGLE/4)
        
        for num in range(0,ran):
            GPIO.output(self.PIN_A, GPIO.HIGH)
            GPIO.output(self.PIN_B, GPIO.HIGH)
            sleep(self.SPEED)
            GPIO.output(self.PIN_A, GPIO.LOW)
            GPIO.output(self.PIN_B, GPIO.HIGH)
            sleep(self.SPEED)
            GPIO.output(self.PIN_A, GPIO.LOW)
            GPIO.output(self.PIN_B, GPIO.LOW)
            sleep(self.SPEED)
            GPIO.output(self.PIN_A, GPIO.HIGH)
            GPIO.output(self.PIN_B, GPIO.LOW)
            sleep(self.SPEED)
        GPIO.output(self.POWER, GPIO.LOW)

    def left(self, angle=180):
        GPIO.output(self.POWER, GPIO.HIGH)
        ran = int(angle/self.BASE_STEP_ANGLE/4)
        
        for num in range(0, ran):
            GPIO.output(self.PIN_A, GPIO.HIGH)
            GPIO.output(self.PIN_B, GPIO.HIGH)
            sleep(self.SPEED)
            GPIO.output(self.PIN_A, GPIO.HIGH)
            GPIO.output(self.PIN_B, GPIO.LOW)
            sleep(self.SPEED)
            GPIO.output(self.PIN_A, GPIO.LOW)
            GPIO.output(self.PIN_B, GPIO.LOW)
            sleep(self.SPEED)
            GPIO.output(self.PIN_A, GPIO.LOW)
            GPIO.output(self.PIN_B, GPIO.HIGH)
            sleep(self.SPEED)
        GPIO.output(self.POWER, GPIO.LOW)

    def stop(self):
        GPIO.output(self.POWER, GPIO.LOW)

def main():

    turret = Turret()
    try:
        turret.right(160)
        sleep(1)
        turret.left(160)
        sleep(1)
    except KeyboardInterrupt:
        pass

    turret.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    main()