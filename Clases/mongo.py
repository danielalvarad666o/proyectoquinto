import os
import time
import pymongo
import json 
from Clases.JSON import Jsonn
class MongoDBClient(Jsonn):
    def __init__(self, uri):
        super().__init__()
        self.lista2=[]
        self.uri = uri
        self.client=None
        
    
    def connect(self):
        urls = [self.uri, "mongodb://54.175.50.139:27018/?directConnection=true"]
        for url in urls:
            try:
                client = pymongo.MongoClient(url, serverSelectionTimeoutMS=2000, directConnection=True)
                client.server_info()  # Intente obtener información del servidor
                self.client = client
                print("Conexión exitosa a MongoDB")
                return True
            except pymongo.errors.ConnectionFailure as e:
                print(f"No se puede conectar a {url}: {e}")
        print("No se puede conectar a ningún servidor")
        return False

   
    
    
    
    def update_all_documents(self, db_name, coll_name, new_docs):
        try:
            if os.path.exists("temp.json"):
                
                with open('temp.json','r') as file:
                    listatempo=json.load(file)
                for kk in listatempo:
                  self.lista2=kk
                for mm in new_docs:
                  self.lista2=mm
                db = self.client[db_name]
                coll = db[coll_name]
                coll.insert_many(self.lista2)
                os.remove("temp.json")
                  
            else:
             db = self.client[db_name]
             coll = db[coll_name]
             coll.insert_many(new_docs)
             
            
      
        except Exception as e:
              
              # print("No se puede conectar a ningún servidor")
               for j in new_docs:
                   self.lista2.append({"Clave":format(j.get('Clave')),"Sensor":format(j.get('Sensor')),"Value":format(j.get('Value')),"Fecha":format(j.get('Fecha'))})
                
               print(self.lista2)
             
             
              # if os.path.exists("temp.json"):
              #  self.agregarjson(self.lista2,"temp")
              # else: 
              #   self.crearjson(self.lista2,"temp")
              
        # If the update fails, write new_docs to "temp.json"
         
            