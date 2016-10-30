#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webiopi

GPIO = webiopi.GPIO

class Track():

    PWM_L = 21
    PWM_R = 13

    IN_A_L = 20
    IN_B_L = 26
    IN_A_R = 19
    IN_B_R = 16


    def __init__(self):

        # left PWM
        GPIO.setFunction(self.PWM_L, GPIO.PWM)
        # left OUT
        GPIO.setFunction(self.IN_A_L, GPIO.OUT)
        GPIO.setFunction(self.IN_B_L, GPIO.OUT)

        # right PWM
        GPIO.setFunction(self.PWM_R, GPIO.PWM)
        # rightt OUT
        GPIO.setFunction(self.IN_A_R, GPIO.OUT)
        GPIO.setFunction(self.IN_B_R, GPIO.OUT)

        GPIO.pwmWrite(self.PWM_L, 50)
        GPIO.pwmWrite(self.PWM_R, 50)

    def stop(self):
        GPIO.pwmWrite(self.PWM_L, 0)
        GPIO.pwmWrite(self.PWM_R, 0)

        GPIO.digitalWrite(self.IN_A_L, GPIO.LOW);
        GPIO.digitalWrite(self.IN_B_L, GPIO.LOW);
        GPIO.digitalWrite(self.IN_A_R, GPIO.LOW);
        GPIO.digitalWrite(self.IN_B_R, GPIO.LOW);

    def brake(self):
        GPIO.pwmWrite(self.PWM_L, 100);
        GPIO.pwmWrite(self.PWM_R, 100);

        GPIO.digitalWrite(self.IN_A_L, GPIO.HIGH);
        GPIO.digitalWrite(self.IN_B_L, GPIO.HIGH);
        GPIO.digitalWrite(self.IN_A_R, GPIO.HIGH);
        GPIO.digitalWrite(self.IN_B_R, GPIO.HIGH);

    def straight(self, speed):
        GPIO.pwmWrite(self.PWM_L, speed);
        GPIO.pwmWrite(self.PWM_R, speed);

        GPIO.digitalWrite(self.IN_A_L, GPIO.HIGH);
        GPIO.digitalWrite(self.IN_B_L, GPIO.LOW);
        GPIO.digitalWrite(self.IN_A_R, GPIO.HIGH);
        GPIO.digitalWrite(self.IN_B_R, GPIO.LOW);

    def back(self, speed):
        GPIO.pwmWrite(self.PWM_L, speed);
        GPIO.pwmWrite(self.PWM_R, speed);

        GPIO.digitalWrite(self.IN_A_L, GPIO.LOW);
        GPIO.digitalWrite(self.IN_B_L, GPIO.HIGH);
        GPIO.digitalWrite(self.IN_A_R, GPIO.LOW);
        GPIO.digitalWrite(self.IN_B_R, GPIO.HIGH);

    def turn(self, speedR, speedL):
        GPIO.pwmWrite(self.PWM_L, speedR);
        GPIO.pwmWrite(self.PWM_R, speedL);

        GPIO.digitalWrite(self.IN_A_L, GPIO.HIGH);
        GPIO.digitalWrite(self.IN_B_L, GPIO.LOW);
        GPIO.digitalWrite(self.IN_A_R, GPIO.HIGH);
        GPIO.digitalWrite(self.IN_B_R, GPIO.LOW);

    def pivotTurnRight(self, speed):
        GPIO.pwmWrite(self.PWM_L, speed);
        GPIO.pwmWrite(self.PWM_R, speed);

        GPIO.digitalWrite(self.IN_A_L, GPIO.HIGH);
        GPIO.digitalWrite(self.IN_B_L, GPIO.LOW);
        GPIO.digitalWrite(self.IN_A_R, GPIO.LOW);
        GPIO.digitalWrite(self.IN_B_R, GPIO.HIGH);

    def pivotTurnLeft(self, speed):
        GPIO.pwmWrite(self.PWM_L, speed);
        GPIO.pwmWrite(self.PWM_R, speed);

        GPIO.digitalWrite(self.IN_A_L, GPIO.LOW);
        GPIO.digitalWrite(self.IN_B_L, GPIO.HIGH);
        GPIO.digitalWrite(self.IN_A_R, GPIO.HIGH);
        GPIO.digitalWrite(self.IN_B_R, GPIO.LOW);
