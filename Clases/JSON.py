import json

class Jsonn:
    

               #guaradar en el archivo exitente
   def crearjson(self ,diccionario,elnombre):
     with open(elnombre+'.json','w') as file:
         json.dump(diccionario,file,indent=5)
   
  
         
   def leerjson(self,nombredelarchivo):    
      with open(nombredelarchivo+'.json','r') as file:
       return json.load(file)
     
   def elmpatyjson(self,nombredelarchivo):  
    try:
      with open(nombredelarchivo+'.json','r') as file:
        json.load(file)
        return True
    except:
      return False
    
   def agregarjson(self, diccionario, nombredelarchivo):
        try:
            with open(nombredelarchivo+'.json', 'r+') as file:
                data = json.load(file)
                data.update(diccionario)
                file.seek(0)
                json.dump(data, file, indent=5)
        except:
            with open(nombredelarchivo+'.json', 'w') as file:
                json.dump(diccionario, file, indent=5)
     