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

class Menu(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Menú Principal")
        self.geometry("400x400")
        self.resizable(False, False)
        self.config(bg="blue")

        label_menu = tk.Label(self, text="Menú Principal", font=("Arial", 16), bg="blue", fg="white")
        label_menu.pack(pady=20)

        button_opcion1 = tk.Button(self, text="Opción 1", command=self.mostrar_opcion1)
        button_opcion1.pack(pady=10)

        button_opcion2 = tk.Button(self, text="Opción 2", command=self.mostrar_opcion2)
        button_opcion2.pack(pady=10)

        button_opcion3 = tk.Button(self, text="Opción 3", command=self.mostrar_opcion3)
        button_opcion3.pack(pady=10)

        button_opcion4 = tk.Button(self, text="Opción 4", command=self.mostrar_opcion4)
        button_opcion4.pack(pady=10)

        button_opcion5 = tk.Button(self, text="Opción 5", command=self.mostrar_opcion5)
        button_opcion5.pack(pady=10)

        button_salir = tk.Button(self, text="Salir", command=self.salir_sistema)
        button_salir.pack(pady=10)



    def mostrar_opcion1(self):
        messagebox.showinfo("Materias del plan", "\n" + "Año | Dic. | Materia | Se cursa | Se rinde |\n" +
                            "1 | 1c | Matemática | Si | Si |\n" +
                            "1 | 1c | Programación 1 | Si | Si |\n" +
                            "1 | 1c | Sistemas de Procesamiento de Datos | Si | Si |\n" +
                            "1 | 1c | Inglés 1 | Si | Si |\n" +
                            "1 | 1c | Laboratorio de computación 1 | Si | Si |\n" +
                            "1 | 2c | Programación 2 | Si | Si |\n" +
                            "1 | 2c | Arquitectura y Sistemas Operativos | Si | Si |\n" +
                            "1 | 2c | Estadística | Si | Si |\n" +
                            "1 | 2c | Inglés 2 | Si | Si |\n" +
                            "1 | 2c | Laboratorio de computación 2 | Si | Si |\n" +
                            "1 | 2c | Metodología de la investigación | Si | Si |\n")
        self.cerrar_ventana()

    def mostrar_opcion2(self):
        messagebox.showinfo("Estado Académico", "\n" + "Año | Materia | Estado |\n" +
                            "1 | Matemática | Cursa |\n" +
                            "1 | Programación 1 | Cursa |\n" +
                            "1 | Sistemas de Procesamiento de Datos | Cursa |\n" +
                            "1 | Inglés 1 | Cursa |\n" +
                            "1 | Laboratorio de computación 1 | Cursa |\n" +
                            "1 | Programación 2 | |\n" +
                            "1 | Arquitectura y Sistemas Operativos | |\n" +
                            "1 | Estadística | |\n" +
                            "1 | Inglés 2 | |\n" +
                            "1 | Laboratorio de computación 2 | |\n" +
                            "1 | Metodología de la investigación | |\n")
        self.cerrar_ventana()

    def mostrar_opcion3(self):
        messagebox.showinfo("Correlatividad", "\n" + "Año | Materia | Correlatividad |\n" +
                            "1 | Matemática | Puede Cursar |\n" +
                            "1 | Programación 1 | Puede Cursar |\n" +
                            "1 | Sistemas de Procesamiento de Datos | Puede Cursar |\n" +
                            "1 | Inglés 1 | Puede Cursar |\n" +
                            "1 | Laboratorio de computación 1 | Puede Cursar |\n" +
                            "1 | Programación 2 | No cursó Programación 1-Laboratorio de computación 1 |\n" +
                            "1 | Arquitectura y Sistemas Operativos | No cursó Sistemas de Procesamiento de Datos |\n" +
                            "1 | Estadística | No cursó Matemática |\n" +
                            "1 | Inglés 2 | No cursó Inglés 1 |\n" +
                            "1 | Laboratorio de computación 2 | No cursó Programación 1-Laboratorio de computación 1 |\n" +
                            "1 | Metodología de la investigación | |\n")
        self.cerrar_ventana()

    def mostrar_opcion4(self):
        messagebox.showinfo("Correlatividad Rendir", "\n" +
                            "Año | Materia | Correlatividad |\n" +
                            "1 | Matemática | No regularizó |\n" +
                            "1 | Programación 1 | No regularizó |\n" +
                            "1 | Sistemas de Procesamiento de Datos | No regularizó |\n" +
                            "1 | Inglés 1 | No regularizó |\n" +
                            "1 | Laboratorio de computación 1 | No regularizó |\n" +
                            "1 | Programación 2 | No regularizó Programación 1-Laboratorio de computación 1 |\n" +
                            "1 | Arquitectura y Sistemas Operativos | No regularizó Sistemas de Procesamiento de Datos |\n" +
                            "1 | Estadística | No regularizó Matemática |\n" +
                            "1 | Inglés 2 | No regularizó Inglés 1 |\n" +
                            "1 | Laboratorio de computación 2 | No regularizó Programación 1-Laboratorio de computación 1 |\n" +
                            "1 | Metodología de la investigación | No regularizó |\n")
        self.cerrar_ventana()

    def mostrar_opcion5(self):
        messagebox.showinfo("Correlatividades para rendir", "\n" +
                            "Examenes\n" +
                            "Fecha | Materia | Nota | Especialidad |")
        self.cerrar_ventana()

    def salir_sistema(self):
        self.master.destroy()

    def cerrar_menu_principal(self):
        self.destroy()
        self.master.deiconify()


class InicioSesion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de Sesión")
        self.geometry("500x300")
        self.resizable(False, False)
        self.config(bg="blue")

        label_bienvenida = tk.Label(self, text="Facultad Regional San Rafael\nSistema Académico SYSACAD\nMódulo de autogestión alumnos",
                                    font=("Arial", 12), bg="blue", fg="white")
        label_bienvenida.pack(pady=10)

        label_usuario = tk.Label(self, text="Ingrese usuario:", font=("Arial", 12), bg="blue", fg="white")
        label_usuario.pack(pady=10)
        self.entry_usuario = tk.Entry(self, width=70)
        self.entry_usuario.pack(pady=5)

        label_contrasena = tk.Label(self, text="Ingrese contraseña:", font=("Arial", 12), bg="blue", fg="white")
        label_contrasena.pack(pady=10)
        self.entry_contrasena = tk.Entry(self, width=70, show="*")
        self.entry_contrasena.pack(pady=5)

        button_ingresar = tk.Button(self, text="Ingresar", command=self.verificar_credenciales)
        button_ingresar.pack(pady=10)

    def verificar_credenciales(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        conexion = psycopg2.connect(
            user='postgres',
            password='admin',
            host='127.0.0.1',
            database='usuarios',
            port='5432',
        )

        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s", (usuario, contrasena))
            resultado = cursor.fetchone()
            cursor.close()

            if resultado:
                self.abrir_menu_principal()
            else:
                messagebox.showerror("Error", "Credenciales incorrectas")
        except psycopg2.Error as e:
            print("Error al conectarse a la base de datos:", e)
            messagebox.showerror("Error", "Error al conectarse a la base de datos")

        conexion.close()

    def abrir_menu_principal(self):
        self.withdraw() 
        menu_principal = Menu(self) 
        self.mainloop()



app = InicioSesion()

app.mainloop()
