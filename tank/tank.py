#! /usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
import wiringpi
from parts.track import Track
from parts.turret import Turret
from parts.cannon import Cannon


def main():

    track = Track();
    turret = Turret();
    cannon = Cannon();

    try:
        while True:

            if True:
                track.straight(100);
                sleep(3)

                track.stop();
                sleep(1)

                turret.right(90)
                
                sleep(0.5)
                cannon.setAngle(79)
                
                track.back(100);
                sleep(3)

                track.stop();
                sleep(1)

                turret.left(90)
                
                sleep(0.5)
                cannon.setAngle(99)

                track.turn(100,0);
                sleep(1)

                track.stop();
                sleep(1)

                turret.right(180)
                
                sleep(0.5)
                cannon.setAngle(89)

                track.turn(0,100);
                sleep(1)

                track.stop();
                sleep(1)

                turret.left(180)
                
                sleep(0.5)
                cannon.setAngle(119)

                track.pivotTurnRight(100)
                sleep(3)

                track.stop();
                sleep(1)

                track.pivotTurnLeft(100)
                sleep(3)            

                track.stop();
                sleep(1)
                
                sleep(0.5)
                cannon.setAngle(89)
                
                print("end")
                sleep(3)

    except KeyboardInterrupt:
        pass

    GPIO.cleanup()

if __name__ == "__main__":
    main()
