import tkinter as tk
from tkinter import messagebox
import psycopg2

#Camila
class MenuPrincipal(tk.Toplevel):
        def __init__(self):
            super().__init__()
            self.title("Menú Principal")
            self.geometry("500x300")
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
#Nicolas
class Opcion1Window(tk.Toplevel):
        def __init__(self, menu_principal):
            super().__init__()
            self.title("Opción 1")
            self.geometry("400x250")
            self.config(bg="blue")
            self.protocol("WM_DELETE_WINDOW", self.cerrar_opcion)
            self.menu_principal = menu_principal

            self.label = tk.Label(self,
                                  text="Materias del plan" + "\n" + "Año | Dic. | Materia | Se cursa | Se rinde |\n" +
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
                                       "1 | 2c | Metodología de la investigación | Si | Si |\n",font=("Arial", 16), bg="blue", fg="white")
            self.label.pack(pady=10)

        def cerrar_opcion(self):
            self.destroy()  # Cerrar la ventana de la opción 1
            self.menu_principal.deiconify()  # Mostrar nuevamente la ventana del menú principal

class Opcion2Window(tk.Toplevel):
        def __init__(self, menu_principal):
            super().__init__()
            self.title("Opción 2")
            self.geometry("400x250")
            self.config(bg="blue")
            self.protocol("WM_DELETE_WINDOW", self.cerrar_opcion)
            self.menu_principal = menu_principal

            self.label = tk.Label(self, text="Estado Académico" + "\n" + "Año | Materia | Estado |\n" +
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
                                             "1 | Metodología de la investigación | |\n",font=("Arial", 16), bg="blue", fg="white")
            self.label.pack(pady=10)

        def cerrar_opcion(self):
            self.destroy()  # Cerrar la ventana de la opción 2
            self.menu_principal.deiconify()

class Opcion3Window(tk.Toplevel):
        def __init__(self, menu_principal):
            super().__init__()
            self.title("Opción 3")
            self.geometry("400x250")
            self.config(bg="blue")
            self.protocol("WM_DELETE_WINDOW", self.cerrar_opcion)
            self.menu_principal = menu_principal

            self.label = tk.Label(self, text="Correlatividad" + "\n" + "Año | Materia | Correlatividad |\n" +
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
                                             "1 | Metodología de la investigación | |\n",font=("Arial", 16), bg="blue", fg="white")
            self.label.pack(pady=10)

        def cerrar_opcion(self):
            self.destroy()  # Cerrar la ventana de la opción 3
            self.menu_principal.deiconify()

class Opcion4Window(tk.Toplevel):
        def __init__(self, menu_principal):
            super().__init__()
            self.title("Opción 4")
            self.geometry("400x250")
            self.config(bg="blue")
            self.protocol("WM_DELETE_WINDOW", self.cerrar_opcion)
            self.menu_principal = menu_principal

            self.label = tk.Label(self, text="Correlatividad Rendir" + "\n" +
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
                                             "1 | Metodología de la investigación | No regularizó |\n",font=("Arial", 16), bg="blue", fg="white")
            self.label.pack(pady=10)

        def cerrar_opcion(self):
            self.destroy()  # Cerrar la ventana de la opción 4
            self.menu_principal.deiconify()

class Opcion5Window(tk.Toplevel):
        def __init__(self, menu_principal):
            super().__init__()
            self.title("Opción 5")
            self.geometry("400x250")
            self.config(bg="blue")
            self.protocol("WM_DELETE_WINDOW", self.cerrar_opcion)
            self.menu_principal = menu_principal

            self.label = tk.Label(self,
                                  text="Correlatividades para rendir" + "\n" + "Examenes\n" + "|Fecha | Materia | Nota | Especialidad |",font=("Arial", 16), bg="blue", fg="white")
            self.label.pack(pady=10)

        def cerrar_opcion(self):
            self.destroy()  # Cerrar la ventana de la opción 5
            self.menu_principal.deiconify()



#Nahuel
class InicioSesion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de Sesión")
        self.geometry("500x300")
        self.resizable(False, False)
        self.config(bg="blue")

        label_bienvenida = tk.Label(self,
                                    text="Facultad Regional San Rafael\nSistema Académico SYSACAD\nMódulo de autogestión alumnos",
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
#Ayelen
    def verificar_credenciales(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        # Verificar las credenciales en la base de datos
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
        self.withdraw()  # Ocultar la ventana de inicio de sesión
        menu_principal = MenuPrincipal()  # Crear la ventana del menú principal
        self.mainloop()


app = InicioSesion()

app.mainloop()
