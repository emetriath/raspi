# -*- coding: utf-8 -*-
from time import sleep
import wiringpi

pinSrv = 12;

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(pinSrv, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(375)

wiringpi.pwmWrite(pinSrv,50)

#S35 STD
rightcyc = 70
leftcyc  = 80 
stop = 75

list = [rightcyc, stop, leftcyc, stop]

try:
    while True:
        for duty in list:
            wiringpi.pwmWrite(pinSrv, duty)
            if duty == stop:
                sleep(1)
            else:
                sleep(3)

except KeyboardInterrupt:
    pass

