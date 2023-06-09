import tkinter
import tkinter as tk
from tkcalendar import Calendar
from ..Entity import Llamada

def mostrar_vista_home():
    # Ocultar la vista 2 y mostrar la vista home
    vista_consultar_encuesta.pack_forget()
    vista_home.pack()


def mostrar_vista_consultar_encuesta():
    # Ocultar la vista home y mostrar la vista consultar encuesta
    vista_home.pack_forget()
    vista_consultar_encuesta.pack()


# Crear la ventana principal
root = tk.Tk()
root.title("IVR")
root.geometry("600x400")

# Crear la vista home
vista_home = tk.Frame(root)
etiqueta_home = tk.Label(vista_home, text="Bienvenido al Sistema de Respuesta de Voz Interactiva (IVR)")
etiqueta_home.pack()

# Imagen vista home
img = tkinter.PhotoImage(file="../logo.png")
img = img.subsample(2)
lbl_img = tkinter.Label(vista_home, image=img)
lbl_img.pack()

# Crear la vista consultar encuesta
vista_consultar_encuesta = tk.Frame(root)
etiqueta_consultar_encuesta = tk.Label(vista_consultar_encuesta, text="Consultar encuesta")
etiqueta_consultar_encuesta.grid(row=0, columnspan=2, padx=10, pady=10)

# Label para FechaDesde
label_fecha_desde = tk.Label(vista_consultar_encuesta, text="FechaDesde")
label_fecha_desde.grid(row=1, column=0, padx=10, pady=5)

# Calendario Desde
calDesde = Calendar(vista_consultar_encuesta, selectmode='day',
                    year=datetime.datetime.now().year, month=datetime.datetime.now().month,
                    day=(datetime.datetime.now().day - 5))
calDesde.grid(row=2, column=0, padx=10, pady=5)

# Label para FechaHasta
label_fecha_hasta = tk.Label(vista_consultar_encuesta, text="FechaHasta")
label_fecha_hasta.grid(row=1, column=1, padx=10, pady=5)

# Calendario hasta
calHasta = Calendar(vista_consultar_encuesta, selectmode='day',
                    year=datetime.datetime.now().year, month=datetime.datetime.now().month,
                    day=datetime.datetime.now().day)
calHasta.grid(row=2, column=1, padx=10, pady=5)

def get_selected_date():
    desde_date = calDesde.get_date()
    hasta_date = calHasta.get_date()
    date_label.config(text=f"Fechas seleccionadas: Desde: {desde_date}, Hasta: {hasta_date}")

# Botón para obtener las fechas seleccionadas
button = tk.Button(vista_consultar_encuesta, text="Obtener fechas seleccionadas", command=get_selected_date)
button.grid(row=3, columnspan=2, padx=10, pady=10)

# Label para mostrar las fechas seleccionadas
date_label = tk.Label(vista_consultar_encuesta, text="")
date_label.grid(row=4, columnspan=2, padx=10, pady=10)

# Listado de llamadas (datos simulados)
llamadas = [
    Llamada("Operador 1", "Acción requerida 1", 10, True, "Observación 1", [], [], None),
    Llamada("Operador 2", "Acción requerida 2", 5, False, "Observación 2", [], [], None),
    Llamada("Operador 3", "Acción requerida 3", 8, True, "Observación 3", [], [], None)
]

# Widget para mostrar el listado de llamadas
llamadas_listbox = tk.Listbox(vista_consultar_encuesta)
llamadas_listbox.grid(row=5, columnspan=2, padx=10, pady=10)

# Configurar datos de las llamadas en el widget
for llamada in llamadas:
    llamadas_listbox.insert(tk.END, llamada.descripcionOperador)

# Crear botones para cambiar las vistas
boton_vista_home = tk.Button(root, text="Home", command=mostrar_vista_home)
boton_vista_home.pack()

boton_vista_consultar_encuesta = tk.Button(root, text="Consultar Encuesta", command=mostrar_vista_consultar_encuesta)
boton_vista_consultar_encuesta.pack()


# Mostrar la vista inicial (home)
mostrar_vista_home()

# Ejecutar la aplicación
root.mainloop()
