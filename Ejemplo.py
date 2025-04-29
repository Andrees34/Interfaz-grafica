# Se escribe el codigo inicial de la interfaz 
# Para ello se realizara a traves de la libreria "tkinter"

from tkinter import*

raiz=Tk()

# Asignacion de metodos

raiz.title("Ventana de pruebas")

# Codigo para que no se pueda cambiar de tamaño la ventana
raiz.resizable(0,0)

# Codigo introduccion icono aplicacion

raiz.iconbitmap("icono.ico.ico")

# Asignar dimensiones de la ventana
raiz.geometry("550x600")

# Asignar color de la ventana
raiz.config(bg="green")

raiz.mainloop()
