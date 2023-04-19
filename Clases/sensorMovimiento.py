import RPi.GPIO as GPIO
import time

class MotionSensor:
    def __init__(self, led_pin, pir_pin):
        self.led_pin = led_pin
        self.pir_pin = pir_pin
        self.setup()
    
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.setup(self.pir_pin, GPIO.IN)
    
    def wait_for_motion(self):
        value = GPIO.input(self.pir_pin)
        if value == GPIO.HIGH:
            GPIO.output(self.led_pin, GPIO.HIGH)
            time.sleep(5)  # LED stays on for 5 seconds
            GPIO.output(self.led_pin, GPIO.LOW)
            return True
        else:
            GPIO.output(self.led_pin, GPIO.LOW)
            return False

