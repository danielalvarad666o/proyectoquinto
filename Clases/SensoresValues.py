import datetime
import math
import os
from Clases.Lista import lista


class Sensor(lista):
    def __init__(self):
        super().__init__()
        self.lista2=[]  
        self.temp_dict={}
        self.temp=[]
        
   
 
    def crearsensorvalue(self,line,sesnorinfo):  
           for line in line.splitlines():
             parts = line.split(":")
             if len(parts) == 2:
               if str(parts[0]) == "Temperatura 0 ":
                  
                   self.temp_dict={"Clave":"kkkl","Sensor":{"Clave":sesnorinfo[0].get('Clave'),"Tipo":sesnorinfo[0].get('Tipo'),"Ubicacion":sesnorinfo[0].get('Ubicacion'),"Pines":sesnorinfo[0].get('Pines')},"Value":parts[1],"Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                   self.lista.append(self.temp_dict)
                   
               elif str(parts[0])=="Humedad 0 ":
                   self.temp_dict={"Clave":"pppp","Sensor":{"Clave":sesnorinfo[6].get('Clave'),"Tipo":sesnorinfo[6].get('Tipo'),"Ubicacion":sesnorinfo[6].get('Ubicacion'),"Pines":sesnorinfo[6].get('Pines')},"Value":parts[1],"Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                   self.lista.append(self.temp_dict)
               elif str(parts[0])=="Temperatura 1 ":
                   self.temp_dict={"Clave":"HHHH","Sensor":{"Clave":sesnorinfo[1].get('Clave'),"Tipo":sesnorinfo[1].get('Tipo'),"Ubicacion":sesnorinfo[1].get('Ubicacion'),"Pines":sesnorinfo[1].get('Pines')},"Value":parts[1],"Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                   self.lista.append(self.temp_dict)
               elif str(parts[0])=="Humedad 1 ":
                   self.temp_dict={"Clave":"kojd","Sensor":{"Clave":sesnorinfo[7].get('Clave'),"Tipo":sesnorinfo[7].get('Tipo'),"Ubicacion":sesnorinfo[7].get('Ubicacion'),"Pines":sesnorinfo[7].get('Pines')},"Value":parts[1],"Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                   self.lista.append(self.temp_dict)
                   
                   
               elif str(parts[0])=="gas 1 ":
                   
                   self.temp_dict={"Clave":sesnorinfo[2].get('Clave'),"Sensor":{"Clave":sesnorinfo[2].get('Clave'),"Tipo":sesnorinfo[2].get('Tipo'),"Ubicacion":sesnorinfo[2].get('Ubicacion'),"Pines":sesnorinfo[2].get('Pines')},"Value":parts[1],"Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                   self.lista.append(self.temp_dict)
                   
               
               elif str(parts[0])=="Distncia 0 ":
                   
                   self.temp_dict={"Clave":sesnorinfo[4].get('Clave'),"Sensor":{"Clave":sesnorinfo[4].get('Clave'),"Tipo":sesnorinfo[4].get('Tipo'),"Ubicacion":sesnorinfo[4].get('Ubicacion'),"Pines":sesnorinfo[4].get('Pines')},"Value":parts[1],"Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                   self.lista.append(self.temp_dict)
                
             
             self.guardar(self.lista,"sensorValue")
           return self.lista
    
    def crearsensorvalue1(self,line,sesnorinfo):
           
           for line in line.splitlines():
             parts = line.split(":")
             if len(parts) == 2:
               if str(parts[0]) == "Temperatura 0 ":
                  
                   self.temp_dict={"Clave":"kkkl","Sensor":{"Clave":sesnorinfo[0].get('Clave'),"Tipo":sesnorinfo[0].get('Tipo'),"Ubicacion":sesnorinfo[0].get('Ubicacion'),"Pines":sesnorinfo[0].get('Pines')},"Value":parts[1],"Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                   self.lista.append(self.temp_dict)
                   
               elif str(parts[0])=="Humedad 0 ":
                   self.temp_dict={"Clave":"pppp","Sensor":{"Clave":sesnorinfo[6].get('Clave'),"Tipo":sesnorinfo[6].get('Tipo'),"Ubicacion":sesnorinfo[6].get('Ubicacion'),"Pines":sesnorinfo[6].get('Pines')},"Value":parts[1],"Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                   self.lista.append(self.temp_dict)
               elif str(parts[0])=="Temperatura 1 ":
                   self.temp_dict={"Clave":"HHHH","Sensor":{"Clave":sesnorinfo[1].get('Clave'),"Tipo":sesnorinfo[1].get('Tipo'),"Ubicacion":sesnorinfo[1].get('Ubicacion'),"Pines":sesnorinfo[1].get('Pines')},"Value":parts[1],"Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                   self.lista.append(self.temp_dict)
               elif str(parts[0])=="Humedad 1 ":
                   self.temp_dict={"Clave":"kojd","Sensor":{"Clave":sesnorinfo[7].get('Clave'),"Tipo":sesnorinfo[7].get('Tipo'),"Ubicacion":sesnorinfo[7].get('Ubicacion'),"Pines":sesnorinfo[7].get('Pines')},"Value":parts[1],"Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                   self.lista.append(self.temp_dict)
                   
                   
               elif str(parts[0])=="gas 1 ":
                   
                   self.temp_dict={"Clave":sesnorinfo[2].get('Clave'),"Sensor":{"Clave":sesnorinfo[2].get('Clave'),"Tipo":sesnorinfo[2].get('Tipo'),"Ubicacion":sesnorinfo[2].get('Ubicacion'),"Pines":sesnorinfo[2].get('Pines')},"Value":parts[1],"Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                   self.lista.append(self.temp_dict)
                   
               
               elif str(parts[0])=="Distncia 0 ":
                   
                   self.temp_dict={"Clave":sesnorinfo[4].get('Clave'),"Sensor":{"Clave":sesnorinfo[4].get('Clave'),"Tipo":sesnorinfo[4].get('Tipo'),"Ubicacion":sesnorinfo[4].get('Ubicacion'),"Pines":sesnorinfo[4].get('Pines')},"Value":parts[1],"Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                   self.lista.append(self.temp_dict)
               elif str(parts[0]=="Luz 0 "):
                   self.temp_dict={"Clave":sesnorinfo[3].get('Clave'),"Sensor":{"Clave":sesnorinfo[3].get('Clave'),"Tipo":sesnorinfo[3].get('Tipo'),"Ubicacion":sesnorinfo[3].get('Ubicacion'),"Pines":sesnorinfo[3].get('Pines')},"Value":parts[1],"Fecha": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                   self.lista.append(self.temp_dict)
             
               for j in self.lista:
                  self.lista2.append({"Clave":j.get('Clave'),"Sensor":j.get('Sensor'),"Value":j.get('Value'),"Fecha":j.get('Fecha')})
            
            
               if os.path.exists("temp.json"):
                 self.temp=self.leerjson("temp")
                 print(self.temp)
                 for i in self.temp:
                  self.lista2.append(i)
                 self.crearjson(self.lista2,"temp")
               else:
                 self.crearjson(self.lista2,"temp")
            
             
                   
           
           
                   
                   
           
