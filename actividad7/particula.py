from algoritmos import distacia_euclidiana


class Particula:
    def __init__ (self, id=0, origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0, red="", green="", blue="",distancia=0):
        self.__id=id
        self.__origen_x=origen_x
        self. __origen_y=origen_y
        self. __destino_x= destino_x
        self. __destino_y=destino_y
        self. __velocidad=velocidad
        self. __red=red
        self. __green=green
        self. __blue=blue
        self. __distancia=distacia_euclidiana(origen_x,origen_y,destino_x,destino_y)

    #covertir todos los atributos a un string para poderlos imprimir
    def __str__(self):
        return(
            'id: '+ str (self.__id) + '\n'+
            'origen x: '+ str (self.__origen_x) + '\n'+
            'origen y: '+ str( self.__origen_y )+ '\n'+
            'destino x: '+str(self.__destino_x) + '\n'+
            'destino y: '+ str(self.__destino_y) + '\n'+
            'velocidad: '+str(self.__velocidad)+ '\n'+
            'red: '+str(self.__red) + '\n'+
            'green: '+str(self.__green)+ '\n'+
            'blue: '+str(self.__blue )+ '\n'+
            'distancia: '+str(self.__distancia) + '\n' 
        )

    def to_dict(self):
        return{
            "id":self.__id,
            "origen x ": self.__origen_x,
            "origen y ": self.__origen_y,
            "destono x": self.__destino_x,
            "destino y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red ": self.__red,
            "green": self.__green,
            "blue": self.__blue,
            "distancia": self.__distancia

        }


#crear objeto
#p01=Particula(id=1,origen_x=10, origen_y=23,destino_x=10,destino_y=1,velocidad=20,red="Rojo",green="Verde", blue="azul",distancia=distacia_euclidiana)
#print(p01)
#p02=Particula(2,3,4,5,6,7,"color", "color","color", distacia_euclidiana)
#print(p02)
