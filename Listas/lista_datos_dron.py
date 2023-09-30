from Listas.nodo_dato_dron import nodo_dato_dron

class lista_dato_dron:

    def __init__(self):
        self.primero =None
        self.contador = 0

    def agregar_dron(self,Dato_dron):
        if self.primero is None:
            self.primero = nodo_dato_dron(dato_dron=Dato_dron)
            self.contador +=1
            return
        temp = self.primero
        while temp.siguiente:
            temp = temp.siguiente
        temp.siguiente =  nodo_dato_dron(dato_dron=Dato_dron)
        self.contador += 1

    def recorrer_lista(self):
        print("=============================")
        temp =self.primero
        while temp != None:
            print("Dron: ", temp.Dato_dron.dron)
            temp.Dato_dron.lista_valores.recorrer_valores_drones()
            temp = temp.siguiente
        print("==============================")
