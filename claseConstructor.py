#CLASE
class Aprendiz():
    #nombre='Lina'
    #apellido='Barrios'
    #edad=18
    
    #CONSTRUCTOR
    def __init__(self, nom, ape, eda):
        self.nombre=nom
        self.apellido=ape
        self.edad=eda

aprendiz1= Aprendiz('Lina','Barrios',18)
print(aprendiz1.nombre, aprendiz1.apellido, aprendiz1.edad)

aprendiz2= Aprendiz('Jersson','Barrios',22)
print(aprendiz2.nombre, aprendiz2.apellido, aprendiz2.edad)