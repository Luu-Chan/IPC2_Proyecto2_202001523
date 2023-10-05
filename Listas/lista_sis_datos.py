from Listas.nodo_sis_datos import nodo_sis_datos
import os

class lista_sis_datos:

    def __init__(self):
        self.primero = None
        self.contador = 0
    
    def agregar_sis_datos(self, altura):
        nuevo_nodo = nodo_sis_datos(valores_sis=altura)

        if self.contador == 0:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            actual = self.primero
            anterior = None
            while actual is not None and (int(actual.valores_sis.altura) < int(nuevo_nodo.valores_sis.altura) | (int(actual.valores_sis.altura) == int(nuevo_nodo.valores_sis.altura) & int(actual.valores_sis.contador) < int(nuevo_nodo.valores_sis.contador))):
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
            else:
                nuevo_nodo.siguiente = actual
                anterior.siguiente = nuevo_nodo

        self.contador += 1
    

    def recorrer_valores_drones(self):
        print("==========================\n")
        temp = self.primero
        while temp:
            print("Alturas: ", temp.valores_sis.altura, "Caracter : ", temp.valores_sis.letra)
            temp = temp.siguiente
        print("==========================\n")

    def delete(self):
        while self.primero:
            temp = self.primero
            self.primero = self.primero.siguiente
            del temp
            