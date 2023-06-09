import datetime
import RPi.GPIO as GPIO
import time

class MotionSensor:
    def __init__(self, led_pin, pir_pin):
        self.dicionario={}
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
        
    def dicionariovalue(self,tipo):
         self.dicionario={"Clave":tipo[5].get('Clave'),"Sensor":{"Clave":tipo[5].get('Clave'),"Tipo":tipo[5].get('Tipo'),"Ubicacion":tipo[5].get('Ubicacion'),"Pines":tipo[5].get('Pines')},"Value":"1","Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
         return self.dicionario
     
    def notdicionariovalue(self,tipo):
         self.dicionario={"Clave":tipo[5].get('Clave'),"Sensor":{"Clave":tipo[5].get('Clave'),"Tipo":tipo[5].get('Tipo'),"Ubicacion":tipo[5].get('Ubicacion'),"Pines":tipo[5].get('Pines')},"Value":"0","Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
         return self.dicionario

