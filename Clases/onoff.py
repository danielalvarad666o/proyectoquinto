from sseclient import SSEClient
from led import LEDController
from rueda import MotorDriver
import requests

class Controller:
    def __init__(self) -> None:
        self.status = True
        self.led = LEDController(16)
        self.motor = MotorDriver()
        self.motor.stop()
    
    def changeStatus(self) -> None:
        while True:
            self.eventHandler()
    
    def eventHandler(self) -> None:
        message = SSEClient('http://192.168.252.152:3333/led/stream')
        print(message)
        if(message):
            self.requestStatus()

    def requestStatus(self) -> None:
        print('Request Step')
        response = requests.get('http://192.168.252.152:3333/led/status/1')
        data = response.json()
        status = data['status']
        if status == 1:
            self.motor.go_right()
        else:
            self.motor.stop()

if __name__ == '__main__':
    controller = Controller()
    controller.changeStatus()