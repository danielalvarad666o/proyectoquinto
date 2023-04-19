import serial
import serial.tools.list_ports
import json

class SensorData:
    def __init__(self, baudrate=9600):
        port=serial.tools.list_ports.comports()
        portList=[]
        for ports in port:
            portList.append(str(ports)) 
            print(str(portList))
        val=input("Escojer un COM: ")
        try:
         print("conectado serial")
         self.serial_port = serial.Serial(val, baudrate)
        except:
          print("EL puerto o serial no esta conectado")
            
    def read_sensor_data(self):
        self.line = self.serial_port.readline().decode().strip()
        return self.line
