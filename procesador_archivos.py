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
                lista_dron_xml = xml_data.findall("listaDrones")
                for datos_xml in lista_dron_xml:
                    lista_drns = datos_xml.findall("dron")
                    for xml_text in lista_drns:
                        valor = xml_text.text
                        dato = Dron(valor)
                        self.lista_temp_drones.agregar_dron(dato)
                self.lista_temp_drones.recorrer()

        except Exception as e:
            print("Error", e) 