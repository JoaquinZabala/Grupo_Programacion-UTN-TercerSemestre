import tkinter as tk
from tkinter import messagebox
import psycopg2

class MenuPrincipal(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Menú Principal")
        self.geometry("400x250")
        self.resizable(False, False)
        self.config(bg="blue")
        self.label = tk.Label(self, text="Seleccione una opción:")
        self.label.pack(pady=10)

        self.button1 = tk.Button(self, text="Opción 1", command=self.mostrar_opcion1)
        self.button1.pack()

        self.button2 = tk.Button(self, text="Opción 2", command=self.mostrar_opcion2)
        self.button2.pack()

        self.button3 = tk.Button(self, text="Opción 3", command=self.mostrar_opcion3)
        self.button3.pack()

        self.button4 = tk.Button(self, text="Opción 4", command=self.mostrar_opcion4)
        self.button4.pack()

        self.button5 = tk.Button(self, text="Opción 5", command=self.mostrar_opcion5)
        self.button5.pack()

        self.button6 = tk.Button(self, text="Salir", command=self.mostrar_opcion6)
        self.button6.pack()


    def mostrar_opcion1(self):
        self.withdraw()  # Ocultar la ventana del menú
        opcion1_window = Opcion1Window(self)  # Crear una nueva ventana para la opción 1

    def mostrar_opcion2(self):
        self.withdraw()
        opcion2_window = Opcion2Window(self)  # Crear una nueva ventana para la opción 2

    def mostrar_opcion3(self):
        self.withdraw()
        opcion3_window = Opcion3Window(self)  # Crear una nueva ventana para la opción 3

    def mostrar_opcion4(self):
        self.withdraw()
        opcion3_window = Opcion4Window(self)  # Crear una nueva ventana para la opción 4

    def mostrar_opcion5(self):
        self.withdraw()
        opcion3_window = Opcion5Window(self)  # Crear una nueva ventana para la opción 5

    def mostrar_opcion6(self):
        self.destroy()
        self.master.deiconify()
