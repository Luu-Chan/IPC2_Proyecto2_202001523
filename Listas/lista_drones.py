import os

import graphviz
from Listas.nodo_drones import nodo_drones


class lista_dron:

    def __init__(self):
        self.primero = None
        self.siguiente = None
        self.contador = 0



    def agregar_dron(self, dron):
        nuevo_nodo = nodo_drones(Dron=dron)
        if self.contador == 0 or self.primero.Dron.nombre >= dron.nombre:
            nuevo_nodo.siguiente = self.primero
            self.primero = nuevo_nodo
        else:
            temp = self.primero
            while temp.siguiente is not None and temp.siguiente.Dron.nombre < dron.nombre:
                temp = temp.siguiente
            nuevo_nodo.siguiente = temp.siguiente
            temp.siguiente = nuevo_nodo
        self.contador += 1

    def agregar_dron_desornedado(self, dron):
        nuevo_nodo = nodo_drones(Dron=dron)
        if self.contador == 0:
            self.primero = nuevo_nodo
            
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
        
    def generar_dot(self):
        dot_code = 'digraph G {\n'
        temp = self.primero
        while temp is not None:
            dot_code += f'  "{temp.Dron.nombre}"->'
            temp = temp.siguiente
        dot_code += 'Listado_de_Drones'
        dot_code += '}'
        print(dot_code)
        return dot_code
    
    def delete(self):
        while self.primero:
            temp = self.primero
            self.primero = self.primero.siguiente
            del temp
            
