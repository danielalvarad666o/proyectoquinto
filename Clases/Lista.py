from Clases.JSON import Jsonn 

class lista(Jsonn):    
    def __init__(self): 
       self.lista=[]
       
    def guardar(self,dicionario,nombre):
       self.crearjson(dicionario,nombre)
      
       
    def append(self,objeto):
       self.lista.append(objeto)
   
    def datosdeljson(self,elnombredelarchivo):
     return super().leerjson(elnombredelarchivo)
    
   
         
       
    def eliminar(self,lista,elcaracter,nombre):
       posicion=0
       existe=False
       for ObjetoaEliminar in lista:
           if ObjetoaEliminar.get(nombre)==elcaracter:
             print("se elimino el objeto: ")
             print(ObjetoaEliminar)
             existe=True
             print()
             lista.pop(posicion)
             return True
           else:
             posicion=posicion+1
       if existe==False:
           return False
        
    # def eliminarV(self,lista,elcaracter):
    #    posicion=0
    #    existe=False
    #    for ObjetoaEliminar in lista:
    #        if ObjetoaEliminar.get("Cliente")==elcaracter:
    #          print("se elimino el objeto: ")
    #          print(ObjetoaEliminar)
    #          existe=True
    #          print()
    #          lista.pop(posicion)
    #          return True
    #        else:
    #          posicion=posicion+1
    #    if existe==False:
    #        return False
        
    def buscar(self,lista,buscar):
       posicion=0
       existe=False
       for objetosaBuscar in lista:
          if objetosaBuscar.get("nombre")==buscar:
           existe=True
           return objetosaBuscar
          else:
           posicion=posicion+1
       if existe==False:
          return False
       
    def modificar(self,lista,propiedad,buscarelvalor,nuevovalor):
       exiteeldato=False
       for objetos in lista:
          if objetos.get(propiedad)==buscarelvalor:
             exiteeldato=True
             objetos[propiedad]=nuevovalor
             return objetos
       if exiteeldato==False:
          return "No se encontro el valor"