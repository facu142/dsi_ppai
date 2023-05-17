import tkinter as tk

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

# Crear la vista 1
vista_1 = tk.Frame(root)
etiqueta_1 = tk.Label(vista_1, text="Vista 1")
etiqueta_1.pack()

# Crear la vista 2
vista_2 = tk.Frame(root)
etiqueta_2 = tk.Label(vista_2, text="Preguntas aaaaaaaaaaaaaa")
etiqueta_2.pack()

# Crear botones para cambiar las vistas
boton_vista_1 = tk.Button(root, text="Mostrar Vista 1", command=mostrar_vista_1)
boton_vista_1.pack()

boton_vista_2 = tk.Button(root, text="Mostrar Vista 2", command=mostrar_vista_2)
boton_vista_2.pack()

# Mostrar la vista inicial
mostrar_vista_1()

# Ejecutar la aplicación
root.mainloop()
