from simplejson import JSONEncoderForHTML
from particula import Particula
from algoritmos import distacia_euclidiana
import json
class Admin:
    def __init__(self):
        self. __almacen=[]


    def agregar_final(self, particula:Particula):
        self. __almacen.append(particula)

    def agregar_inicio(self, particula:Particula):
        self. __almacen.insert(0, particula)

    def mostrar(self):
        for particula in self.__almacen:
            print(particula)   

    def __str__(self):
        return "".join(
            str(admin)+ "\n" for admin in self.__almacen )

    def save(self, ubicacion):
        try:

            with open(ubicacion, 'w') as archivo:
                # archivo.write(str(self))
                lista= [Particula.to_dict() for Particula in self.__almacen]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0
    def open(self, ubicacion):
        try:
            with open(ubicacion, "r") as archivo:
                lista=json.load(archivo)
                self.__almacen=[Particula(**Particula) for Particula in lista ]
            return 1
        except:
            return 0 
        




#p01=Particula(id=1,origen_x=10, origen_y=23,destino_x=10,destino_y=1,velocidad=20,red="Rojo",green="Verde", blue="azul",distancia=distacia_euclidiana)
#p02=Particula(2,3,4,5,6,7,"color", "color","color", distacia_euclidiana)
#particula=Admin()
#particula.agregar_final(p01)
#particula.agregar_inicio(p02)
#particula.agregar_inicio(p01)
#particula.mostrar()