from Listas.nodo_sis_drones import nodo_sis_drones
import os


class lista_sis_drones:
    
    def __init__(self) :
        self.primero = None
        self.contador = 0

    
    def agregar_sis_drones(self,sis_drones):
        if self.primero is None:
            self.primero = nodo_sis_drones(sis_dns=sis_drones)
            self.contador += 1
            return
        
        temp = self.primero
        while temp.siguiente:
            temp = temp.siguiente
        temp.siguiente = nodo_sis_drones(sis_dns=sis_drones)
        self.contador += 1

    def recorrer(self):
        temp = self.primero
        print("===========================\n")
        while temp:
            print("nombre: ", temp.sis_dns.nombre, "alturas: ",temp.sis_dns.altura, "cantidad de drones:", temp.sis_dns.cantidad_dns)
            temp.sis_dns.lista_datos_dron.recorrer_lista()
            temp = temp.siguiente
        print("===========================\n")

