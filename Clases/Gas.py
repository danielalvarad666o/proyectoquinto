from Clases.Lista import lista

class Gas(lista):
    def __init__(self):
        super().__init__()
        
      
    def crearsesnor(self,Tipo,Ubicacion,Pines,Clave):
        return{"Clave":Clave,"Tipo":Tipo,"Ubicacion":Ubicacion,"Pines":Pines}