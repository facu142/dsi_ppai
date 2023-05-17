import tkinter as tk

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")
        self.root.geometry('400x400')
        
        # Botón para abrir la segunda ventana
        btn_abrir = tk.Button(root, text="Consultar encuesta", command=self.abrir_segunda_ventana)
        btn_abrir.pack()
      
    def abrir_segunda_ventana(self):
        # Crear una instancia de la segunda ventana
        ventana_secundaria = tk.Toplevel(self.root)
        ventana_secundaria.title("Segunda Ventana")
        
        # Resto del código para configurar la segunda ventana
        # ...

# Crear la ventana principal
root = tk.Tk()
ventana_principal = VentanaPrincipal(root)

# Iniciar el bucle principal de la aplicación
root.mainloop()




