from tkinter import *
import os
import tkinter as tk
from tkinter import messagebox,filedialog
from procesador_archivos import procesador_archivos


class app:
    def __init__(self, root):

        #Configuraciones de la ventana inicial
        self.path = ''
        self.root = root
        self.root.title("Menu")
        self.root.resizable(False,False)
        self.root.config(cursor="hand2")
        self.root.geometry("1200x600")
        self.root.config(bg="SlateBlue1")
        self.root.config(bd="30")
        self.root.config(relief="groove")
        self.manejador= procesador_archivos()


        self.bt_datos=Button(self.root,text="Ayuda",font=("Comic Sans MS",8),bg="white",fg="black")
        self.bt_datos.grid(row=3, column=8,padx=10)
        self.bt_datos.config(command=self.ayuda)

        self.bt_abrir = Button(self.root, text="Abrir Archivo", bg="white", fg="black", relief=RAISED)
        self.bt_abrir.grid(row=3, column=2,padx=10)
        self.bt_abrir.config(command=self.cargar_archivo)

        self.bt_proc = Button(self.root, text="Procesar Archivo", bg="white", fg="black", relief=RAISED)
        self.bt_proc.grid(row=5, column=2,padx=15)
        self.bt_proc.config(command= self.procesar_el_archivo)

        self.bt_drones = Button(self.root, text="Listado de Drones", bg="white", fg="black", relief=RAISED)
        self.bt_drones.grid(row=3, column=4,padx=10)
        self.bt_drones.config(command=self.graph)

        self.bt_agregar_d = Button(self.root, text="Agregar Dron", bg="white", fg="black", relief=RAISED)
        self.bt_agregar_d.grid(row=3, column=6,padx=10)


    def ayuda(self):
        messagebox.showinfo(title="<System Help>",message="Luis Gabriel Lopez Polanco - 202001523")
    
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

if __name__ == "__main__":
    root = tk.Tk()
    app = app(root)
    root.mainloop()