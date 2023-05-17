import tkinter as tk
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
root.geometry("600x400")

# Crear la vista 2
vista_1 = tk.Frame(root)
etiqueta_1 = tk.Label(vista_1, text="Home")
etiqueta_1.pack()

# Crear la vista 2
vista_2 = tk.Frame(root)
etiqueta_2 = tk.Label(vista_2, text="Consultar encuesta")
etiqueta_2.grid(row=0, columnspan=2, padx=10, pady=10)

# Label para FechaDesde
label_fecha_desde = tk.Label(vista_2, text="FechaDesde")
label_fecha_desde.grid(row=1, column=0, padx=10, pady=5)

# Calendario Desde
calDesde = Calendar(vista_2, selectmode='day',
                    year=2020, month=5,
                    day=22)
calDesde.grid(row=2, column=0, padx=10, pady=5)

# Label para FechaHasta
label_fecha_hasta = tk.Label(vista_2, text="FechaHasta")
label_fecha_hasta.grid(row=1, column=1, padx=10, pady=5)

# Calendario hasta
calHasta = Calendar(vista_2, selectmode='day',
                    year=datetime.datetime.now().year, month=datetime.datetime.now().month,
                    day=datetime.datetime.now().day)
calHasta.grid(row=2, column=1, padx=10, pady=5)

def get_selected_date():
    desde_date = calDesde.get_date()
    hasta_date = calHasta.get_date()
    date_label.config(text=f"Fechas seleccionadas: Desde: {desde_date}, Hasta: {hasta_date}")

# Botón para obtener las fechas seleccionadas
button = tk.Button(vista_2, text="Obtener fechas seleccionadas", command=get_selected_date)
button.grid(row=3, columnspan=2, padx=10, pady=10)

# Label para mostrar las fechas seleccionadas
date_label = tk.Label(vista_2, text="")
date_label.grid(row=4, columnspan=2, padx=10, pady=10)


# Crear botones para cambiar las vistas
boton_vista_1 = tk.Button(root, text="Home", command=mostrar_vista_1)
boton_vista_1.pack()

boton_vista_2 = tk.Button(root, text="Consultar Encuesta", command=mostrar_vista_2)
boton_vista_2.pack()


# Mostrar la vista inicial
mostrar_vista_1()

# Ejecutar la aplicación
root.mainloop()
