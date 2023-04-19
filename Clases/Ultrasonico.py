from Clases.Lista import lista

class Ultrasonico(lista):
    def __init__(self):
        super().__init__()
        
    
    def crearsesnor(self,Tipo,Ubicacion,trigger_pin,echo_pin,Clave):
       return ({"Clave":Clave,"Tipo":Tipo,"Ubicacion":Ubicacion,"Pines":"trigger_pin: {}, echo_pin: {}".format(trigger_pin,echo_pin)})