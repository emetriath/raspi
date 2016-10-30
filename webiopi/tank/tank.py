#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/pi/dev/webiopi/htdocs/app/tank')
import webiopi
from time import sleep
from parts.track import Track
from parts.turret import Turret
from parts.cannon import Cannon
from parts.fire import Fire


webiopi.setDebug()
webiopi.debug(sys.path)

track = Track()
turret = Turret()
cannon = Cannon()
fire = Fire()

#state
wheelMode = 0
wheelSpeed = 0
turretMove = False
turretDiection = 0

def setup():
    webiopi.debug("Script with macros - Setup")

def loop():

    try:
        # stop
        if(wheelMode == 0):
            track.stop()
        # straight
        elif wheelMode == 1:
            track.straight(wheelSpeed)
        # left
        elif wheelMode == 2:
            track.turn(0,wheelSpeed)
        # right
        elif wheelMode == 3:
            track.turn(wheelSpeed,0)
        # back
        elif wheelMode == 4:
            track.back(wheelSpeed)
        # pivot Left
        elif wheelMode == 5:
            track.pivotTurnLeft(wheelSpeed)
        #  pivot Right
        elif wheelMode == 6:
            track.pivotTurnRight(wheelSpeed)

        if turretMove:
            if turretDiection == 0:
                #stop
                turret.stop()
            elif turretDiection == 1:
                #left
                turret.left()
            elif turretDiection == 2:
                #right
                turret.right()

    except KeyboardInterrupt:
        destroy()

def destroy():
    webiopi.debug("Script with macros - Destroy")
    global track
    track.stop()

@webiopi.macro
def setWheel(mode, speed):
    webiopi.debug("Script with macros - setWheel ")
    global wheelMode, wheelSpeed
    wheelMode = int(mode)
    wheelSpeed = int(speed)

@webiopi.macro
def setTurret(angle):
    webiopi.debug("Script with macros - setTurret ")
    global turretDiection, turretMove
    turretDiection = int(angle)
    if turretDiection == 0:
        #stop
        turretMove = False
    elif turretDiection == 1:
        #left
        turretMove = True
    elif turretDiection == 2:
        #right
        turretMove = True

@webiopi.macro
def gunfire(num):
    global fire
    fire.fire(int(num))