import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import datetime
from Entity import *

def mostrar_vista_home():
    vista_consultar_encuesta.pack_forget()
    vista_home.pack()

def mostrar_vista_consultar_encuesta():
    vista_home.pack_forget()
    vista_consultar_encuesta.pack()

root = tk.Tk()
root.title("IVR")
root.geometry("600x400")

vista_home = tk.Frame(root)
etiqueta_home = tk.Label(vista_home, text="Bienvenido al Sistema de Respuesta de Voz Interactiva (IVR)")
etiqueta_home.pack()

img = tk.PhotoImage(file="logo.png")
img = img.subsample(2)
lbl_img = tk.Label(vista_home, image=img)
lbl_img.pack()

vista_consultar_encuesta = tk.Frame(root)
etiqueta_consultar_encuesta = tk.Label(vista_consultar_encuesta, text="Consultar encuesta")
etiqueta_consultar_encuesta.grid(row=0, columnspan=2, padx=10, pady=10)

label_fecha_desde = tk.Label(vista_consultar_encuesta, text="FechaDesde")
label_fecha_desde.grid(row=1, column=0, padx=10, pady=5)

calDesde = Calendar(vista_consultar_encuesta, selectmode='day',
                    year=datetime.datetime.now().year, month=datetime.datetime.now().month,
                    day=(datetime.datetime.now().day - 5))
calDesde.grid(row=2, column=0, padx=10, pady=5)

label_fecha_hasta = tk.Label(vista_consultar_encuesta, text="FechaHasta")
label_fecha_hasta.grid(row=1, column=1, padx=10, pady=5)

calHasta = Calendar(vista_consultar_encuesta, selectmode='day',
                    year=datetime.datetime.now().year, month=datetime.datetime.now().month,
                    day=datetime.datetime.now().day)
calHasta.grid(row=2, column=1, padx=10, pady=5)

def get_selected_date():
    desde_date = calDesde.get_date()
    hasta_date = calHasta.get_date()
    date_label.config(text=f"Fechas seleccionadas: Desde: {desde_date}, Hasta: {hasta_date}")

button = tk.Button(vista_consultar_encuesta, text="Obtener fechas seleccionadas", command=get_selected_date)
button.grid(row=3, columnspan=2, padx=10, pady=10)

date_label = tk.Label(vista_consultar_encuesta, text="")
date_label.grid(row=4, columnspan=2, padx=10, pady=10)

llamadas = [
    Llamada("Operador 1", "Acción requerida 1", 10, True, "Observación 1", [], [], None),
    Llamada("Operador 2", "Acción requerida 2", 5, False, "Observación 2", [], [], None),
    Llamada("Operador 3", "Acción requerida 3", 8, True, "Observación 3", [], [], None)
]

llamadas_treeview = ttk.Treeview(vista_consultar_encuesta)
llamadas_treeview.grid(row=5, columnspan=2, padx=10, pady=10)

llamadas_treeview["columns"] = ("descripcionOperador", "detalleAccionRequerida", "duracion",
                                "encuestaEnviada", "observacionAuditor")

llamadas_treeview.heading("descripcionOperador", text="Descripción Operador")
llamadas_treeview.heading("detalleAccionRequerida", text="Detalle Acción Requerida")
llamadas_treeview.heading("duracion", text="Duración")
llamadas_treeview.heading("encuestaEnviada", text="Encuesta Enviada")
llamadas_treeview.heading("observacionAuditor", text="Observación Auditor")

for llamada in llamadas:
    llamadas_treeview.insert("", tk.END, text=llamada.descripcionOperador,
                             values=(llamada.descripcionOperador, llamada.detalleAccionRequerida,
                                     llamada.duracion, llamada.encuestaEnviada, llamada.observacionAuditor))

boton_vista_home = tk.Button(root, text="Home", command=mostrar_vista_home)
boton_vista_home.pack()

boton_vista_consultar_encuesta = tk.Button(root, text="Consultar Encuesta", command=mostrar_vista_consultar_encuesta)
boton_vista_consultar_encuesta.pack()

mostrar_vista_home()

root.mainloop()
