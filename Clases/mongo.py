import os
import time
import pymongo
import json 
from Clases.JSON import Jsonn
class MongoDBClient(Jsonn):
    def __init__(self, uri):
        self.lista2=[]
        self.uri = uri
        self.client=None
        self.listatempo=[]
    
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
                print("Encontramos temp")
                with open('temp.json','r') as file:
                    self.listatempo=json.load(file)
                db = self.client[db_name]
                coll = db[coll_name]
                coll.insert_many(self.listatempo)
                
                os.remove("temp.json")
            db = self.client[db_name]
            coll = db[coll_name]
         
           # coll.delete_many({})
            coll.insert_many(new_docs)
             
            
      
        except Exception as e:
              print("No se puede conectar a ningún servidor")
              for j in new_docs:
                  self.lista2.append({"Clave":j.get('Clave'),"Sensor":j.get('Sensor'),"Value":j.get('Value'),"Fecha":j.get('Fecha')})
             
              self.crearjson(self.lista2,"temp")
              
        # If the update fails, write new_docs to "temp.json"
         
            