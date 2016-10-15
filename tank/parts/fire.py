import RPi.GPIO as GPIO
from time import sleep

class Fire():

    LED = 4
    
    def __init__(self):
    
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED, GPIO.OUT)
    
    def fire(self,count=1):
        
        for num in range(0, count):
            GPIO.output(self.LED, GPIO.HIGH)
            sleep(0.5)

def main():
    fire = Fire()
    try:
        fire.fire(10)
    except KeyboardInterrupt:
        pass

    GPIO.cleanup()

if __name__ == "__main__":
    main()
