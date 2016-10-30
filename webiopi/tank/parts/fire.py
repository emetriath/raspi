#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webiopi

GPIO = webiopi.GPIO

class Fire():

    LED = 4

    def __init__(self):
        GPIO.setFunction(self.LED, GPIO.OUT)

    def fire(self, count=1):

        for num in range(0, count):
            GPIO.digitalWrite(self.LED, GPIO.HIGH)
            webiopi.sleep(0.5)

