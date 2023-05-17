import tkinter as tk
from tkinter import *
from tkcalendar import Calendar
import datetime


def mostrar_vista_1():
    # Ocultar la vista 2 y mostrar la vista 1
    vista_2.pack_forget()
    vista_1.pack()


def mostrar_vista_2():
    # Ocultar la vista 1 y mostrar la vista 2
    vista_1.pack_forget()
    vista_2.pack()


# Crear la ventana principal
root = tk.Tk()
root.title("Navegación con Tkinter")
root.geometry("400x700")

# Crear la vista 1
vista_1 = tk.Frame(root)
etiqueta_1 = tk.Label(vista_1, text="Vista 1: Consultar encuesta")

# Calendario Desde
calDesde = Calendar(vista_1, selectmode='day',
                    year=2020, month=5,
                    day=22)

calDesde.pack(pady=20)

# Calendario hasta
calHasta = Calendar(vista_1, selectmode='day',
                    year=datetime.datetime.now().year, month=datetime.datetime.now().month,
                    day=datetime.datetime.now().day)

calHasta.pack(pady=20)


def grad_date():
    date.config(text="Selected Date is: " + calDesde.get_date())


# Add Button and Label
Button(vista_1, text="Obtener fecha seleccionado",
       command=grad_date).pack(pady=20)

date = Label(vista_1, text="")
date.pack(pady=20)

etiqueta_1.pack()

# Crear la vista 2 Otra
vista_2 = tk.Frame(root)
etiqueta_2 = tk.Label(vista_2, text="Vista 2 ???")
etiqueta_2.pack()

# Crear botones para cambiar las vistas
boton_vista_1 = tk.Button(root, text="Consultar Encuesta (Vista 1)", command=mostrar_vista_1)
boton_vista_1.pack()

boton_vista_2 = tk.Button(root, text="Mostrar Vista 2", command=mostrar_vista_2)
boton_vista_2.pack()

# Mostrar la vista inicial
mostrar_vista_1()

# Ejecutar la aplicación
root.mainloop()
