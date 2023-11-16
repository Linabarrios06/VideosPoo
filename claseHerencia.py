#CLASE
class Persona():
    
    
    def __init__(self, apePat, apeMat, nom): #__init__ es el inicializador para la herencia 
        self.apellidoPaterno=apePat
        self.apellidoMaterno=apeMat
        self.nombre=nom
    
    def MostrarNombre(self):
        txt="{0} {1} {2}" #Estos son las posiciones 
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre ) 
        
class Trabajador(Persona):
    pass
#OBJETOS 
trabaj1=Trabajador('Barrios','Cordoba','Arquimedes')
print(trabaj1.MostrarNombre())  
#Ya se creo el objeto 
trabaj2=Trabajador('Hernandez','Guzman','Yaneth')
print(trabaj2.MostrarNombre())  
 
