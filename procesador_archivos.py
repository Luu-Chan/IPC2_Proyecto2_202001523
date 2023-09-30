#from Listas.lista_datos_dron import lista_dato_dron
from Listas.lista_drones import lista_dron
from Listas.lista_datos_dron import lista_dato_dron
from Listas.Drones import Dron
from Listas.Dato_dron import Dato_dron
from Listas.Sis_datos import Sis_datos
from Listas.Sis_drones import Sis_drones
from Listas.lista_sis_datos import lista_sis_datos
from Listas.lista_sis_datos import lista_sis_datos
from Listas.lista_sis_drones import lista_sis_drones
import xml.etree.ElementTree as ET

class procesador_archivos:

    def __init__(self):
        self.lista_temp_drones = lista_dron()
        self.lista_temp_dt = lista_sis_drones()
        

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
                #Recorriendo lista de drones 
                
                sis_drones = xml_data.findall('listaSistemasDrones')
                for xml_sis_dron in sis_drones:
                    sistema_dron = xml_sis_dron.findall('sistemaDrones')
                    for xml_sistema in sistema_dron:
                        nombre = xml_sistema.get('nombre')
                        xml_alturas = xml_sistema.findall('alturaMaxima')
                        for xml_altura_max in xml_alturas:
                            altura_max = xml_altura_max.text
                        xml_cantidad = xml_sistema.findall('cantidadDrones')
                        for xml_cantidad in xml_cantidad:
                            cantidad = xml_cantidad.text
                        contador = 1 
                        lista_temp_altura = lista_sis_datos()
                        xml_drons = xml_sistema.findall('contenido')
                        lista_temp= lista_dato_dron()
                        for data in xml_drons:
                            drones = data.find('dron')
                            dron = drones.text
                            xml_altura = data.findall('alturas')
                            xml_sis_datos = lista_sis_datos()
                            for data_altura in xml_altura:
                                data_altura_dron = data_altura.findall('altura')
                                for altura_valor in data_altura_dron:
                                    altura = altura_valor.get('valor')
                                    letra = altura_valor.text
                                    valores_alturas = Sis_datos(altura,letra,contador)
                                    xml_sis_datos.agregar_sis_datos(valores_alturas)
                            contador += 1  
                            lista_temp.agregar_dron(Dato_dron(dron,xml_sis_datos))
                        print("llenado la segunda")
                        self.lista_temp_dt.agregar_sis_drones(Sis_drones(nombre,altura_max,cantidad,lista_temp))
                        print("antes de recorrer")
                        lista_temp_altura.recorrer_valores_drones()
                    self.lista_temp_dt.recorrer()

        except Exception as e:
            print("Error", e) 