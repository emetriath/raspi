#!/usr/bin/python

import sys;
import numpy as np
import cv2
from time import sleep
import base64
import threading

class Camera():

    htmlimg = "<img src=''>"
    capture = None
    cascade = None
    width = 640
    height = 480
    th_me = None;
    th_run = True;

    def getImage(self):
        return self.htmlimg

    def __init__(self):
        self.cascade = cv2.CascadeClassifier('/home/pi/dev/webiopi/htdocs/app/tank/parts/face.xml')

        self.capture = cv2.VideoCapture(0)
        self.th_run = True
        self.th_me = threading.Thread(target=self.run, name="th_me", args=())
        self.th_me.setDaemon(False)
        self.th_me.start()

    def run(self):

        frame_w = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_h = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        f_center_x = int(frame_w/2)
        f_center_h = int(frame_h/2)

        while(self.capture.isOpened() and self.th_run == True):
            ret, frame = self.capture.read()
            if(ret == True):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.cascade.detectMultiScale(gray, 1.3, 5)
                cv2.circle(frame,(f_center_x,f_center_h),10,(0,0,0,0),2)
                for (x,y,w,h) in faces:
                    center_x = (int(x+w/2))
                    center_h = (int(y+h/2))
                    cv2.circle(frame,(int(x+w/2),int(y+h/2)),int(w/2),(0,255,0),2)
                    cv2.rectangle(frame,(x+int(w/3),y+int(h/3)),(x+w-int(w/3),y+h-int(h/3)),(255,0,0),2)
                    cv2.line(frame,(x+int(w/2),y),(x+int(w/2),y+h),(0,0,255),2)
                    cv2.line(frame,(x,y+int(h/2)),(x+w,y+int(h/2)),(0,0,255),2)
                    msg=str(center_x-f_center_x) + "/" + str(center_h-f_center_h)
                    location=(x,y)
                    fontface=cv2.FONT_HERSHEY_PLAIN
                    fontscale=1.0
                    color=(0,0,0)
                    cv2.putText(frame,msg,location,fontface,fontscale,color)

                cnt = cv2.imencode('.png',frame)[1]
                b64 = base64.b64encode(cnt)

                self.htmlimg = "<img src='data:image/png;base64,"+b64.decode('utf8') +"'>"
                sleep(0.5)

    def stop(self):
        print ("===============stop================")
        self.th_run = False;

if __name__ == '__main__':
    camera = Camera();
    while True:
        camera.getImage();
    camera.stop();
