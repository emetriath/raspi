#! /usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep


p21 = 0
p13 = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)

GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

p21 = GPIO.PWM(21,50)
p13 = GPIO.PWM(13,50)

p21.start(0)
p13.start(0)

try:
    while True:
        p21.ChangeDutyCycle(100);
        p13.ChangeDutyCycle(100);
        GPIO.output(20,1);
        GPIO.output(26,0);
        GPIO.output(19,1);
        GPIO.output(16,0);

        sleep(3)

        p21.ChangeDutyCycle(0);
        p13.ChangeDutyCycle(0);
        GPIO.output(20,0);
        GPIO.output(26,0);
        GPIO.output(19,0);
        GPIO.output(16,0);

        sleep(3)

        p21.ChangeDutyCycle(50);
        p13.ChangeDutyCycle(50);
        GPIO.output(20,0);
        GPIO.output(26,1);
        GPIO.output(19,0);
        GPIO.output(16,1);

        sleep(3)

        p21.ChangeDutyCycle(0);
        p13.ChangeDutyCycle(0);
        GPIO.output(20,0);
        GPIO.output(26,0);
        GPIO.output(19,0);
        GPIO.output(16,0);

        sleep(3)

        p21.ChangeDutyCycle(100);
        p13.ChangeDutyCycle(50);
        GPIO.output(20,1);
        GPIO.output(26,0);
        GPIO.output(19,0);
        GPIO.output(16,1);

        sleep(3)

        p21.ChangeDutyCycle(0);
        p13.ChangeDutyCycle(0);
        GPIO.output(20,0);
        GPIO.output(26,0);
        GPIO.output(19,0);
        GPIO.output(16,0);

        sleep(3)

        p21.ChangeDutyCycle(50);
        p13.ChangeDutyCycle(100);
        GPIO.output(20,0);
        GPIO.output(26,1);
        GPIO.output(19,1);
        GPIO.output(16,0);

        sleep(3)

        p21.ChangeDutyCycle(0);
        p13.ChangeDutyCycle(0);
        GPIO.output(20,0);
        GPIO.output(26,0);
        GPIO.output(19,0);
        GPIO.output(16,0);

        sleep(3)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
