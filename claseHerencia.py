#CLASE
class Persona():
    
    
    def __init__(self, apePat, apeMat, nom):
        self.apellidoPaterno=apePat
        self.apellidoMaterno=apeMat
        self.nombre=nom
    
    def MostrarNombre(self):
        txt="{0} {1} {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre )
        
class Trabajor(Persona):
    pass

trabaj1=Trabajor('Barrios','Cordoba','Arquimedes')
print(trabaj1.MostrarNombre()) 
