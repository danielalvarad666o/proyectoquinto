import RPi.GPIO as GPIO
import time

class MotorDriver:
    def __init__(self, in1_pin=4, in2_pin=5):
        self.in1 = in1_pin
        self.in2 = in2_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        self.stop()


    def go_right(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)

    def go_left(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)

if __name__ == "__main__":
    rueda = MotorDriver()
    rueda.go_right()
    