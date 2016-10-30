#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webiopi

GPIO = webiopi.GPIO

class Turret():

    PIN_A = 23
    PIN_B = 22
    POWER = 27

    BASE_STEP_ANGLE = 1.8;

    SPEED = 0.02

    def __init__(self):

        # IN_A
        GPIO.setFunction(self.PIN_A, GPIO.OUT)
        # IN_B
        GPIO.setFunction(self.PIN_B, GPIO.OUT)

        GPIO.setFunction(self.POWER, GPIO.OUT)

    def right(self, angle = 180):

        GPIO.digitalWrite(self.POWER, GPIO.HIGH)
        ran = int(angle/self.BASE_STEP_ANGLE/4)

        for num in range(0,ran):
            GPIO.digitalWrite(self.PIN_A, GPIO.HIGH)
            GPIO.digitalWrite(self.PIN_B, GPIO.HIGH)
            webiopi.sleep(self.SPEED)
            GPIO.digitalWrite(self.PIN_A, GPIO.LOW)
            GPIO.digitalWrite(self.PIN_B, GPIO.HIGH)
            webiopi.sleep(self.SPEED)
            GPIO.digitalWrite(self.PIN_A, GPIO.LOW)
            GPIO.digitalWrite(self.PIN_B, GPIO.LOW)
            webiopi.sleep(self.SPEED)
            GPIO.digitalWrite(self.PIN_A, GPIO.HIGH)
            GPIO.digitalWrite(self.PIN_B, GPIO.LOW)
            webiopi.sleep(self.SPEED)
        GPIO.digitalWrite(self.POWER, GPIO.LOW)

    def left(self, angle=180):
        GPIO.digitalWrite(self.POWER, GPIO.HIGH)
        ran = int(angle/self.BASE_STEP_ANGLE/4)

        for num in range(0, ran):
            GPIO.digitalWrite(self.PIN_A, GPIO.HIGH)
            GPIO.digitalWrite(self.PIN_B, GPIO.HIGH)
            webiopi.sleep(self.SPEED)
            GPIO.digitalWrite(self.PIN_A, GPIO.HIGH)
            GPIO.digitalWrite(self.PIN_B, GPIO.LOW)
            webiopi.sleep(self.SPEED)
            GPIO.digitalWrite(self.PIN_A, GPIO.LOW)
            GPIO.digitalWrite(self.PIN_B, GPIO.LOW)
            webiopi.sleep(self.SPEED)
            GPIO.digitalWrite(self.PIN_A, GPIO.LOW)
            GPIO.digitalWrite(self.PIN_B, GPIO.HIGH)
            webiopi.sleep(self.SPEED)
        GPIO.digitalWrite(self.POWER, GPIO.LOW)

    def stop(self):
        GPIO.digitalWrite(self.POWER, GPIO.LOW)
