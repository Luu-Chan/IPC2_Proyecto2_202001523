
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
        self.bt_datos.grid(row=0, column=2,padx=10)
        self.bt_datos.config(command=self.ayuda)


    def ayuda(self):
        messagebox.showinfo(title="<System Help>",message="Luis Gabriel Lopez Polanco - 202001523")
    
    


if __name__ == "__main__":
    root = tk.Tk()
    app = app(root)
    root.mainloop()