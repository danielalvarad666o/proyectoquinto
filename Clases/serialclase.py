import serial
import serial.tools.list_ports
import json

class SensorData:
    def __init__(self, baudrate=9600):
        portList = []
        defaultPort = None
        ports = serial.tools.list_ports.comports()
        for port in ports:
            portList.append(port.device)
            if port.device == '/dev/ttyACM0':
                defaultPort = '/dev/ttyACM0'
            print(port.device)

        if defaultPort is None:
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
        else:
            try:
                print("Conectado a", defaultPort)
                self.serial_port = serial.Serial(defaultPort, baudrate)
            except:
                print("Error al conectar al puerto", defaultPort)
            
    def read_sensor_data(self):
        self.line = self.serial_port.readline().decode().strip()
        return self.line
