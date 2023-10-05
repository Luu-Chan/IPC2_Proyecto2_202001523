from tkinter import *
import os
import tkinter as tk
from tkinter import messagebox,filedialog, Label
from tkinter import ttk
from procesador_archivos import procesador_archivos
from Listas.lista_drones import lista_dron
from Listas.Drones import Dron


class app:
    def __init__(self, root):

        #Configuraciones de la ventana inicial
        self.path = ''
        self.root = root
        self.new_dron= ""
        self.root.title("Menu")
        self.root.resizable(False,False)
        self.root.config(cursor="hand2")
        self.root.geometry("1200x600")
        self.root.config(bg="SlateBlue1")
        self.root.config(bd="30")
        self.root.config(relief="groove")
        self.manejador= procesador_archivos()
        self.listtemp = lista_dron()


        self.bt_datos=Button(self.root,text="Ayuda",font=("Comic Sans MS",8),bg="white",fg="black")
        self.bt_datos.grid(row=5, column=10,padx=10)
        self.bt_datos.config(command=self.ayuda)

        self.bt_abrir = Button(self.root, text="Abrir Archivo", bg="white", fg="black", relief=RAISED)
        self.bt_abrir.grid(row=5, column=2,padx=10)
        self.bt_abrir.config(command=self.cargar_archivo)

        self.bt_proc = Button(self.root, text="Procesar Archivo", bg="white", fg="black", relief=RAISED)
        self.bt_proc.grid(row=5, column=4,padx=10)
        self.bt_proc.config(command= self.procesar_el_archivo)

        self.bt_drones = Button(self.root, text="Listado de Drones", bg="white", fg="black", relief=RAISED)
        self.bt_drones.grid(row=5, column=6,padx=10)
        self.bt_drones.config(command=self.graph)

        self.bt_agregar_d = Button(self.root, text="Agregar Dron", bg="white", fg="black", relief=RAISED)
        self.bt_agregar_d.grid(row=5, column=8,padx=10)
        self.bt_agregar_d.config(command=self.ventana_agregar)

        self.bt_delete = Button(self.root, text= "Inicializar", bg="white", fg="black", relief=RAISED )
        self.bt_delete.grid(row= 5, column= 14, padx= 10)
        self.bt_delete.config(command= self.reiniciar)


    def ayuda(self):
        messagebox.showwarning(title="<System Help>",message=" -Luis Gabriel Lopez Polanco\n -Carnet: 202001523\n -IPC2 S2 2023")
    
    def cargar_archivo(self):
        try:
            self.path = filedialog.askopenfilename(filetypes=[("viruz.exe", "*.xml")])
            if not self.path:
                raise ValueError("Archivo no encontrado.")
            messagebox.showinfo("Aviso", "Archivo cargado exitosamente!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def procesar_el_archivo(self):
        try:
            if self.path:
                archivo_n = os.path.basename(self.path)
                self.manejador.procesar_xml(archivo_n)
                messagebox.showinfo("Aviso", "Se proceso el archivo.")
            else:
                messagebox.showerror("Error", "No se seleccionó ningún archivo.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def graph(self):
        self.manejador.graficar()
        print("hola")

    def ventana_agregar(self):
        vtn_nuevo_dron = tk.Toplevel(root)
        vtn_nuevo_dron.title("Listado de drones")
        vtn_nuevo_dron.geometry("500x400")
        etiqueta = tk.Label(vtn_nuevo_dron, text="Ingrese el nuevo dron: ",justify="center")
        etiqueta.pack(pady=20)
        etiqueta_nombre = Label(vtn_nuevo_dron, text="Nombre : ", justify="center")
        etiqueta_nombre.pack()
        entry= Entry(vtn_nuevo_dron)
        entry.pack()
        self.new_dron = entry
        Button(vtn_nuevo_dron, text="Agrega Dron", width=10, height=1, command= self.nuevo_dron).pack(pady=20)
        boton_cerrar = tk.Button(vtn_nuevo_dron, text="Cerrar", command=vtn_nuevo_dron.destroy, fg="black")
        boton_cerrar.pack(side="bottom", pady=10, padx=10)

    def nuevo_dron(self):
        valor = Dron(self.new_dron)
        self.listtemp.agregar_dron(dron=valor)
        messagebox.showinfo("Aviso", " se ha agregado el dron al sistema.")

    def reiniciar(self):
        self.manejador.reiniciar
        self.path = ''
        messagebox.showinfo("Aviso", "se reinicio el windows")


if __name__ == "__main__":
    root = tk.Tk()
    app = app(root)
    root.mainloop()