# -*- coding: utf-8 -*-
from time import sleep
import wiringpi

pinSrv = 12;

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(pinSrv, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(375)

wiringpi.pwmWrite(pinSrv,0)

# TOWER PRO SG90
home = 75
plus90 = 29 
muinus90 = 129 

list = [home]
for x in range(plus90, muinus90+1, 10):
    list.append(x)
list.append(home)

try:
    for duty in list :
        print(duty)
        wiringpi.pwmWrite(pinSrv, int(duty))
        sleep(1)

except KeyboardInterrupt:
    pass

wiringpi.pwmWrite(pinSrv,home)
