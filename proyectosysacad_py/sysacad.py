import tkinter as tk
from tkinter import messagebox
import psycopg2


class Bienvenida(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Bienvenido")
        self.geometry("400x200")
        self.resizable(False, False)
        self.config(bg="blue")

        label_bienvenida = tk.Label(self, text="¡Bienvenido!", font=("Arial", 16), bg="blue", fg="white")
        label_bienvenida.pack(pady=20)

        button_aceptar = tk.Button(self, text="Aceptar", command=self.cerrar_ventana)
        button_aceptar.pack(pady=10)

    def cerrar_ventana(self):
        self.destroy()