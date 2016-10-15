#! /usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
import wiringpi

class Track():

    PWM_L = 0
    PWM_R = 0

    def __init__(self):

        GPIO.setmode(GPIO.BCM)
        # left PWM
        GPIO.setup(21, GPIO.OUT)
        # left OUT
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(26, GPIO.OUT)

        # right PWM
        GPIO.setup(13, GPIO.OUT)
        # rightt OUT
        GPIO.setup(19, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)

        self.PWM_L = GPIO.PWM(21,50)
        self.PWM_R = GPIO.PWM(13,50)

        self.PWM_L.start(0)
        self.PWM_R.start(0)

    def stop(self):
        self.PWM_L.ChangeDutyCycle(0);
        self.PWM_R.ChangeDutyCycle(0);

        GPIO.output(20, GPIO.LOW);
        GPIO.output(26, GPIO.LOW);
        GPIO.output(19, GPIO.LOW);
        GPIO.output(16, GPIO.LOW);

    def brake(self):
        self.PWM_L.ChangeDutyCycle(100);
        self.PWM_R.ChangeDutyCycle(100);

        GPIO.output(20, GPIO.HIGH);
        GPIO.output(26, GPIO.HIGH);
        GPIO.output(19, GPIO.HIGH);
        GPIO.output(16, GPIO.HIGH);

    def straight(self,speed):
        self.PWM_L.ChangeDutyCycle(speed);
        self.PWM_R.ChangeDutyCycle(speed);

        GPIO.output(20, GPIO.HIGH);
        GPIO.output(26, GPIO.LOW);
        GPIO.output(19, GPIO.HIGH);
        GPIO.output(16, GPIO.LOW);

    def back(self,speed):
        self.PWM_L.ChangeDutyCycle(speed);
        self.PWM_R.ChangeDutyCycle(speed);

        GPIO.output(20, GPIO.LOW);
        GPIO.output(26, GPIO.HIGH);
        GPIO.output(19, GPIO.LOW);
        GPIO.output(16, GPIO.HIGH);

    def turn(self,speedR,speedL):
        self.PWM_L.ChangeDutyCycle(speedR);
        self.PWM_R.ChangeDutyCycle(speedL);

        GPIO.output(20, GPIO.HIGH);
        GPIO.output(26, GPIO.LOW);
        GPIO.output(19, GPIO.HIGH);
        GPIO.output(16, GPIO.LOW);

    def pivotTurnRight(self,speed):
        self.PWM_L.ChangeDutyCycle(speed);
        self.PWM_R.ChangeDutyCycle(speed);

        GPIO.output(20, GPIO.HIGH);
        GPIO.output(26, GPIO.LOW);
        GPIO.output(19, GPIO.LOW);
        GPIO.output(16, GPIO.HIGH);

    def pivotTurnLeft(self,speed):
        self.PWM_L.ChangeDutyCycle(speed);
        self.PWM_R.ChangeDutyCycle(speed);

        GPIO.output(20, GPIO.LOW);
        GPIO.output(26, GPIO.HIGH);
        GPIO.output(19, GPIO.HIGH);
        GPIO.output(16, GPIO.LOW);

def main():

    GPIO.setmode(GPIO.BCM)
    track = Track();

    try:
        while True:

            if False:
                print "do"
                gun.stop();
                sleep(1)

            if True:
                track.straight(100);
                sleep(3.0)

                track.stop();
                sleep(1)

                track.back(100);
                sleep(3)

                track.stop();
                sleep(1)

                track.turn(100,0);
                sleep(1)

                track.stop();
                sleep(1)

                track.turn(0,100);
                sleep(1)

                track.stop();
                sleep(1)

                track.pivotTurnRight(100)
                sleep(3)

                track.stop();
                sleep(1)

                track.pivotTurnLeft(100)
                sleep(3)            

                track.stop();
                sleep(1)

    except KeyboardInterrupt:
        pass

    GPIO.cleanup()
    
if __name__ == "__main__":
    main()