import datetime
import math
from Clases.Lista import lista


class Sensor(lista):
    def __init__(self):
        super().__init__()
        self.temp_dict={}
        
   
 
    def crearsensorvalue(self,line,sesnorinfo):  
           for line in line.splitlines():
             parts = line.split(":")
             if len(parts) == 2:
               if str(parts[0]) == "Temperatura 0 ":
                  
                   self.temp_dict={"Clave":sesnorinfo[0].get('Clave'),"Sensor":{"Clave":sesnorinfo[0].get('Clave'),"Tipo":sesnorinfo[0].get('Tipo'),"Ubicacion":sesnorinfo[0].get('Ubicacion'),"Pines":sesnorinfo[0].get('Pines')},"Value":parts[1]}
                   self.lista.append(self.temp_dict)
                   
               elif str(parts[0])=="Humedad 0 ":
                   self.temp_dict={"Clave":sesnorinfo[0].get('Clave'),"Sensor":{"Clave":sesnorinfo[0].get('Clave'),"Tipo":sesnorinfo[0].get('Tipo'),"Ubicacion":sesnorinfo[0].get('Ubicacion'),"Pines":sesnorinfo[0].get('Pines')},"Value":parts[1]}
                   self.lista.append(self.temp_dict)
                   
                   
               elif str(parts[0])=="gas 1 ":
                   
                   self.temp_dict={"Clave":sesnorinfo[2].get('Clave'),"Sensor":{"Clave":sesnorinfo[2].get('Clave'),"Tipo":sesnorinfo[2].get('Tipo'),"Ubicacion":sesnorinfo[2].get('Ubicacion'),"Pines":sesnorinfo[2].get('Pines')},"Value":parts[1]}
                   self.lista.append(self.temp_dict)
                   
               
               elif str(parts[0])=="Distncia 0 ":
                   
                   self.temp_dict={"Clave":sesnorinfo[4].get('Clave'),"Sensor":{"Clave":sesnorinfo[4].get('Clave'),"Tipo":sesnorinfo[4].get('Tipo'),"Ubicacion":sesnorinfo[4].get('Ubicacion'),"Pines":sesnorinfo[4].get('Pines')},"Value":parts[1]}
                   self.lista.append(self.temp_dict)
                
             
             self.guardar(self.lista,"sensorValue")
           return self.lista
                   
           
           
                   
                   
           
