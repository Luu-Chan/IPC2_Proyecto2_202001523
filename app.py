
from tkinter import *
import tkinter as tk
from tkinter import Label,messagebox,filedialog

class app:
    def __init__(self, root):

        #Configuraciones de la ventana inicial
        self.path = ''
        self.root = root
        self.root.title("Menu")
        self.root.resizable(False,False)
        self.root.config(cursor="hand2")
        self.root.geometry("1200x600")
        self.root.config(bg="purple")
        self.root.config(bd="30")
        self.root.config(relief="groove")


        self.bt_datos=Button(self.root,text="Datos del estudiante",font=("Comic Sans MS",10),bg="white",fg="black")
        self.bt_datos.grid(row=2, column=8,padx=10)
        self.bt_datos.config(command=self.ayuda)

        self.bt_abrir = Button(self.root, text="Abrir Archivo", bg="white", fg="black")
        self.bt_abrir.grid(row=2, column=2,padx=10)
        self.bt_abrir.config(command=self.cargar_archivo)

        self.bt_proc = Button(self.root, text="Procesar Archivo", bg="white", fg="black")
        self.bt_proc.grid(row=4, column=2,padx=15)

        self.bt_drones = Button(self.root, text="Listado de Drones", bg="white", fg="black")
        self.bt_drones.grid(row=2, column=4,padx=10)

        self.bt_agregar_d = Button(self.root, text="Agregar Dron", bg="white", fg="black")
        self.bt_agregar_d.grid(row=2, column=6,padx=10)


    def ayuda(self):
        messagebox.showinfo(title="<System Help>",message="Luis Gabriel Lopez Polanco - 202001523")
    
    def cargar_archivo(self):
        try:
            self.path = filedialog.askopenfilename(filetypes=[("Archivos del aux", "*.xml")])
            if not self.path:
                raise ValueError("No selecciono ningún archivo.")
            messagebox.showinfo("Aviso", "Archivo cargado exitosamente!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = app(root)
    root.mainloop()