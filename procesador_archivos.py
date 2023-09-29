#from Listas.lista_datos_dron import lista_dato_dron
from Listas.lista_drones import lista_dron
from Listas.Drones import Dron

import xml.etree.ElementTree as ET



class procesador_archivos:

    def __init__(self):
        self.lista_temp_drones = lista_dron()
        
        

    def procesar_xml(self, ruta):
        try:
            xml_file = open(ruta)
            if xml_file.readable():
                xml_data = ET.fromstring(xml_file.read())

                lst_doc = xml_data.findall("listaDrones")
                
                for datos_xml in lst_doc:
                    lst_doc1 = datos_xml.findall("dron")
                    for docs1 in lst_doc1:
                        valor = docs1.text
                        dato = Dron(valor)
                        self.lista_temp_drones.agregar_dron(dato)
                self.lista_temp_drones.recorrer()

                
        except Exception as rr:
            print("Error", rr) 