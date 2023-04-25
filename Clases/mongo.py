import os
import time
import pymongo
import json 
class MongoDBClient:
    def __init__(self, uri):
        self.uri = uri
    
    def connect(self):
     try:
        self.client = pymongo.MongoClient(self.uri)
        print("Conexión exitosa a MongoDB")
        return self.client
     except Exception as e:
        print("No se puede conectar al primer servidor:", e)

     try:
        self.client = pymongo.MongoClient("mongodb://54.175.50.139:27018/?directConnection=true")
        print("Conexión exitosa a MongoDB")
        return self.client
     except Exception as e:
        print("No se puede conectar al segundo servidor:", e)

     print("No se puede conectar a ningún servidor")
     return False

   
    
    
    
    def update_all_documents(self, db_name, coll_name, new_docs):
        try:
            if os.path.exists("temp.json"):
                listatempo=[]
                with open('temp.json','r') as file:
                    listatempo=json.load(file)
                    db = self.client[db_name]
                    coll = db[coll_name]
                    coll.insert_many(new_docs)
                os.remove("temp.json")
            db = self.client[db_name]
            coll = db[coll_name]
         
           # coll.delete_many({})
            coll.insert_many(new_docs)
             
            
        except Exception as e:
          print("No se pudo establecer una conexión a MongoDB se recomineda restablecer su conexion ")
          with open('temp.json','w') as file:
           json.dump(new_docs,file,indent=5)
          return False
            