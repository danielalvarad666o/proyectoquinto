import requests
from sseclient import SSEClient
from rueda import MotorDriver

class Controller:
    def __init__(self) -> None:
        self.status = True
        self.motor = MotorDriver()
        self.motor.stop()
    
    def changeStatus(self) -> None:
        while True:
            self.eventHandler()
    
    def eventHandler(self) -> None:
        mensaje = SSEClient('http://3.93.149.143:3333/led/stream')
        for msg in mensaje:
            print(msg.data)
            self.requestStatus(msg.data)
    
    def requestStatus(self, data) -> None:
        print('Request Step')
        respuesta = requests.get('http://3.93.149.143:3333/led/update/1')
        status = data['status']
        if status == True:
            self.motor.go_right()
        else:
            self.motor.stop()

if __name__ == '__main__':
    controller = Controller()
    controller.changeStatus()
