import random



from Clases.Lista import lista
class Claves(lista):
    
    
    def __init__(self):
       super().__init__()
        
        
    def crearclaves(self,cantidad):
         cla=[]
         while len(self.lista) < cantidad:
          clave = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=4))
          if clave not in self.lista:
            self.lista.append(clave)
         validacion=super().elmpatyjson("Claves")
         if validacion == False:
             super().crearjson(self.lista,"Claves")
         elif validacion==True:
             cla=super().leerjson("Claves")
             for li in self.lista:
              cla.append(li)
             super().crearjson(cla,"Claves")
            
                
         self.lista=super().leerjson("Claves")   
         return self.lista
     
     
     
