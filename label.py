# Creacion de la libreria "tkinter"

from tkinter import*

root=Tk()

# Creacion de la clase y el constructor
miFrame=Frame(root, width=500, height=400)

miFrame.pack()

# Insercion de una imagen
miImagen=PhotoImage(file="imagen.png")

Label(miFrame, image=miImagen).place(x=10, y=10)

miLabel=Label(miFrame, text="Hola a todos", fg="Blue",font=("Comic Sans Ms", 18)).place(x=0,y=0)

root.mainloop()
