#! /usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep


p21 = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)

GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

p21 = GPIO.PWM(21,50)

p21.start(0)

try:
    while True:
        #forward
        p21.ChangeDutyCycle(100);
        GPIO.output(20,1);
        GPIO.output(26,0);

        sleep(3)

        #stop
        p21.ChangeDutyCycle(0);
        GPIO.output(20,0);
        GPIO.output(26,0);

        sleep(3)

        #back
        p21.ChangeDutyCycle(50);
        GPIO.output(20,0);
        GPIO.output(26,1);

        sleep(3)

        #stop
        p21.ChangeDutyCycle(0);
        GPIO.output(20,0);
        GPIO.output(26,0);

        sleep(3)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
