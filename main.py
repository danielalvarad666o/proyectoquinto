## llamar librerias o clases 
from Clases import mongo,serialclase,Claves,Gas,LDR,Movimiento,Temperatura,Ultrasonico,JSON,SensoresValues,sensorMovimiento

#instanciar 
movimiento=sensorMovimiento.MotionSensor(21,14)
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

sensores=[temperatura1.crearsesnor("DTH11","Dentro de la tienda",11,listadeclaves[2]),
temperatura.crearsesnor("DTH11","Afuera de la tienda",12,listadeclaves[3]),
sensorGas.crearsesnor("GAS","Dentro de la Tienda","A0",listadeclaves[0]),
sensorLuz.crearsesnor("LDR","Techo de la Tienda","A3",listadeclaves[1]),
ultrasonico.crearsesnor("Ultrasonico","Entrada de la tienda",8,9,listadeclaves[4]),elMOVIMIENTO.crearsesnor("PIR","Afuera del parque",14,listadeclaves[5])]

#crear Json sensores info
elJson.crearjson(sensores,"sensoresInfo")



#clinte mongo

sen=sensores

conec=mongo.MongoDBClient("mongodb+srv://root:2tCVgy$_DEa!ZYB@5b.y2llyqd.mongodb.net/test")
con=conec.connect()
conec.update_all_documents("VIDA","SensoresInfo",sensores)

#coneccion 


while True:
     
 
     line=serial.read_sensor_data()
     
     if con: 
        liner=guardardatosdeSensores.crearsensorvalue(line,sen)
        if len(liner)>=1:
             
             print(liner)
             movimiento.wait_for_motion()
             conec.update_all_documents("VIDA","sensoresValue",liner)
             liner.clear()
             
             
        
        
         
       
       
      
     
     
     
     
     
    


    