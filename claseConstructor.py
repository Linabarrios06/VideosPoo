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

#OBJETOS 
aprendiz1= Aprendiz('Lina','Barrios',18)
print(aprendiz1.nombre, aprendiz1.apellido, aprendiz1.edad)

aprendiz2= Aprendiz('Jersson','Barrios',22)
print(aprendiz2.nombre, aprendiz2.apellido, aprendiz2.edad)

aprendiz3= Aprendiz('Kevin','Hernandez',17)
print(aprendiz3.nombre, aprendiz3.apellido, aprendiz3.edad)

aprendiz4= Aprendiz('Sebastian','Pinzon',17)
print(aprendiz4.nombre, aprendiz4.apellido, aprendiz4.edad)

aprendiz5= Aprendiz('Yency','Quiñonez',18)
print(aprendiz5.nombre, aprendiz5.apellido, aprendiz5.edad)
