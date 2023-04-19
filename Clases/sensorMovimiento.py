import RPi.GPIO as GPIO
import time

class MotionSensor:
    def __init__(self, pin):
        self.pin = pin
        self.setup()
    
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
    
    def wait_for_motion(self):
            if GPIO.input(self.pin):
                print("Motion detected!")
                return GPIO.input(self.pin)
                
            time.sleep(0.1)
