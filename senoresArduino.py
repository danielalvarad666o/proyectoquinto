## llamar librerias o clases 
import json
import os
import time
from Clases import mongo,serialclase,Claves,Gas,LDR,Movimiento,Temperatura,Ultrasonico,JSON,SensoresValues,sensorMovimiento,Humedad

#instanciar 
humedad=Humedad.Humedad1()
humedad2=Humedad.Humedad1()
movimiento=sensorMovimiento.MotionSensor(21,4)
serial=serialclase.SensorData()
clavessensores=Claves.Claves()
sensorGas=Gas.Gas()
elJson=JSON.Jsonn()
sensorLuz=LDR.Sensordeluz()
elMOVIMIENTO=Movimiento.Movimientos()
temperatura=Temperatura.Temperatura()
temperatura1=Temperatura.Temperatura()
ultrasonico=Ultrasonico.Ultrasonico()
guardardatosdeSensores=SensoresValues.Sensor()

#iNICIALIZADORES
clavessensores.crearclaves(6)
listadeclaves=clavessensores.lista

sensores=[temperatura1.crearsesnor("Temperatura 1","Dentro de la tienda",11,listadeclaves[2]),
temperatura.crearsesnor("Temperatura 2","Afuera de la tienda",12,listadeclaves[3]),
sensorGas.crearsesnor("GAS","Dentro de la Tienda","A0",listadeclaves[0]),
sensorLuz.crearsesnor("LDR","Techo de la Tienda","A3",listadeclaves[1]),
ultrasonico.crearsesnor("Ultrasonico","Entrada de la tienda",8,9,listadeclaves[4]),
elMOVIMIENTO.crearsesnor("PIR","Afuera del parque",14,listadeclaves[5]),
humedad.crearsesnor("Humedad 1","Dentro de la tienda",11,listadeclaves[2]),
humedad2.crearsesnor("Humedad 2","Afuera de la tienda",12,listadeclaves[3])]

#crear Json sensores info
elJson.crearjson(sensores,"sensoresInfo")



#clinte mongo

sen=sensores





#coneccion 
liner=[]


while True:
     conec=mongo.MongoDBClient("mongodb://54.175.50.139:27017/?directConnection=true")
     if not os.path.exists("sensoresInfo.json"):
      conec.update_all_documents("VIDA","SensoresInfo",sensores)
     con=conec.connect()
     
 
     line=serial.read_sensor_data()
     
     if con: 
        liner=guardardatosdeSensores.crearsensorvalue(line,sen)
        if len(liner)>=1:
             mov=movimiento.wait_for_motion()
             if mov:
                  valores=movimiento.dicionariovalue(sen)
                  liner.append(valores)
             else:
                  valores=valores=movimiento.notdicionariovalue(sen)
                  liner.append(valores)
                  #conec.update_all_documents("VIDA","sensoresValue",valores)
            
             
             conec.update_all_documents("VIDA","sensoresValue",liner)
             
             liner.clear()
     else :
          
          guardardatosdeSensores.crearsensorvalue1(line,sen)
     
          
          
          
     
 
                 
             
        
        
         
       
       
      
     
     
     
     
     
    


    