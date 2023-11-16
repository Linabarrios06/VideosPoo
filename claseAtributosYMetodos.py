#CLASE
class Color:
    
    #ATRIBUTOS
    color='azu' 
    borra= False
    uso_grafico= True
    
    #METODOS
    def colorear(self): #self es la palabra reservada para clasifircar un metodo
        print('El color esta coloreando. ')
        
    def borrar(self):
        if self.se_puede_borrar():
            print('El color esta borrando ')
        else:
            print('El color no puede borrar. ')
        
    def se_puede_borrar(self):
        return self.tiene_borrador
    
#Llamamos los METODOS que hicimos anteriormennte 
color=Color()
color.colorear()
color.tiene_borrador=False #Aqui podemos cambiar el valor ya sea verdadero o falso 
color.borrar()
        




     