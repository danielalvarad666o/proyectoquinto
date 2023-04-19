import serial
import serial.tools.list_ports
import json

class SensorData:
    def __init__(self, baudrate=9600):
        portList = []
        ports = serial.tools.list_ports.comports()
        for port in ports:
            portList.append(port.device)
            print(port.device)

        while True:
            val = input("Selecciona un puerto COM: ")
            if val in portList:
                try:
                    print("Conectado a", val)
                    self.serial_port = serial.Serial(val, baudrate)
                    break
                except:
                    print("Error al conectar al puerto", val)
            else:
                print("Puerto no encontrado, intenta de nuevo.")
            
    def read_sensor_data(self):
        self.line = self.serial_port.readline().decode().strip()
        return self.line
