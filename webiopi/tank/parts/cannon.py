#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wiringpi

class Cannon():

    PIN_PWM = 12;

    # TOWER PRO SG90
    FRONT = 89
    DOWN_LIMIT = 79
    UP_LIMIT = 119

    def __init__(self):

        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self.PIN_PWM, wiringpi.GPIO.PWM_OUTPUT)
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
        wiringpi.pwmSetClock(375)

        wiringpi.pwmWrite(self.PIN_PWM, self.FRONT)

    def setAngle(self, duty):
        wiringpi.pwmWrite(self.PIN_PWM, int(duty))

    def front(self):
        wiringpi.pwmWrite(self.PIN_PWM, self.FRONT)
