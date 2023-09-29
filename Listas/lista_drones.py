
from Listas.nodo_drones import nodo_drones


class lista_dron:

    def __init__(self):
        self.primero = None
        self.contador = 0


    def agregar_dron(self, dron):
        nuevo_nodo = nodo_drones(Dron=dron)
        if self.contador == 0:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            
        else:
            temp = self.primero
            anterior = None
            while temp is not None and temp.Dron.nombre < dron.nombre:
                anterior = temp
                temp = temp.siguiente

            if anterior is None:
                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
            else:
                nuevo_nodo.siguiente = temp
                anterior.siguiente = nuevo_nodo
            
        self.contador += 1


    def recorrer(self):
        print("============================\n")
        temp =  self.primero
        while temp != None:
            print("Nombre: " , temp.Dron.nombre)
            temp = temp.siguiente
        print("======================== \n")


    def eliminar_drones(self):
        while self.primero:
            temp = self.primero
            self.primero = self.primero.siguiente
            del temp
            
