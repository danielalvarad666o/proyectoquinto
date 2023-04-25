import os
import threading
import time
import pymongo
import threading
import json 
from Clases.JSON import Jsonn
class MongoDBClient(Jsonn):
    def __init__(self, uri):
        super().__init__()
        self.lista2=[]
        self.uri = uri
        self.client=None
        
    
    def connect(self):
        urls = [self.uri, "mongodb://54.174.208.18:27018/?directConnection=true"]
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

   
    
    
    
    # def update_all_documents(self, db_name, coll_name, new_docs):
    #     try:
    #         db = self.client[db_name]
    #         coll = db[coll_name]
    #         coll.insert_many(new_docs)
    #         if os.path.exists("temp.json"):
                
    #             with open('temp.json','r') as file:
    #                 listatempo=json.load(file)
    #             if len(listatempo)>=1:
    #              for kk in listatempo:
    #               self.lista2=kk
    #              db = self.client[db_name]
    #              coll = db[coll_name]
    #              coll.insert_many(self.lista2)
                 
                 
    #              os.remove("temp.json") 
                 
            
             
            
      
    #     except Exception as e:
              
    #           print("No se puede conectar a ningún servidor")
        
    #     # Add formatted documents to lista2
    #           self.lista2 = []
    #           otra=[]
    #           for j in new_docs:
    #            self.lista2.append({"Clave": format(j.get('Clave')),
    #                              "Sensor": format(j.get('Sensor')),
    #                              "Value": format(j.get('Value')),
    #                              "Fecha": format(j.get('Fecha'))})
    #           if os.path.exists("temp.json"):
    #              otra=self.leerjson("temp")
    #              for pp in otra:
    #               self.lista2.append(pp)
    #              self.crearjson(self.lista2,"temp")
                  
    #           else: 
    #              self.crearjson(self.lista2,"temp")
        
        # Save documents to temp.json
              
              # print("No se puede conectar a ningún servidor")
              # if len(new_docs)>=1:
              #  for j in new_docs:
              #      self.lista2.append({"Clave":format(j.get('Clave')),"Sensor":format(j.get('Sensor')),"Value":format(j.get('Value')),"Fecha":format(j.get('Fecha'))})
              #      print("")
              #      print(self.lista2)
               
             
             
              #  if os.path.exists("temp.json"):
              #   self.agregarjson(self.lista2,"temp")
              #  else: 
              #   self.crearjson(self.lista2,"temp")
              
        # If the update fails, write new_docs to "temp.json"
        


    def update_all_documents(self, db_name, coll_name, new_docs):
        try:
            db = self.client[db_name]
            coll = db[coll_name]
            coll.insert_many(new_docs)
            if os.path.exists("temp.json"):
              
                with open('temp.json','r') as file:
                    listatempo=json.load(file)
                if len(listatempo)>=1:
                    for kk in listatempo:
                        self.lista2=kk
                    db = self.client[db_name]
                    coll = db[coll_name]
                    coll.insert_many(self.lista2)
                    os.remove("temp.json") 
                
        except Exception as e:
            print("No se puede conectar a ningún servidor")
            self.lista2 = []
            otra=[]
            for j in new_docs:
                self.lista2.append({"Clave": format(j.get('Clave')),
                                    "Sensor": format(j.get('Sensor')),
                                    "Value": format(j.get('Value')),
                                    "Fecha": format(j.get('Fecha'))})
            if os.path.exists("temp.json"):
                otra=self.leerjson("temp")
                for pp in otra:
                    self.lista2.append(pp)
                self.crearjson(self.lista2,"temp")
                
            else: 
                self.crearjson(self.lista2,"temp")
        
        # Crear un hilo para enviar los datos a la base de datos
        t = threading.Thread(target=self._send_data_to_db, args=(db_name, coll_name))
        t.start()
        
    def _send_data_to_db(self, db_name, coll_name):
        db = self.client[db_name]
        coll = db[coll_name]
        if os.path.exists("temp.json"):
            with open('temp.json','r') as file:
                listatempo=json.load(file)
            if len(listatempo)>=1:
                for kk in listatempo:
                    self.lista2=kk
                coll.insert_many(self.lista2)
                os.remove("temp.json") 
        else:
            coll.insert_many(self.lista2)

         
            