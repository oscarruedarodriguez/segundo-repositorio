# oscar ivan rueda rodriguez
# 3° programacion T.M:
# cbtis #89
#muetra nombre y ventana de programacion

import tkinter as tk
from tkinter import Toplevel, Label

# Función para abrir la ventana con el nombre y apellidos
def mostrar_nombre():
    ventana_nombre = Toplevel()
    ventana_nombre.title("Nombre y Apellidos")
    ventana_nombre.geometry("250x100")
    
    # Aquí puedes cambiar tu nombre y apellidos
    Label(ventana_nombre, text="Nombre: Juan", font=("Arial", 12)).pack(pady=5)
    Label(ventana_nombre, text="Apellidos: Pérez García", font=("Arial", 12)).pack(pady=5)

# Función para abrir la ventana con el mensaje "Programado con Python"
def mostrar_mensaje():
    ventana_mensaje = Toplevel()
    ventana_mensaje.title("Mensaje")
    ventana_mensaje.geometry("250x100")

    Label(ventana_mensaje, text="Programado con Python", font=("Arial", 12, "bold")).pack(pady=20)

# Ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("300x150")

# Botones
btn_nombre = tk.Button(ventana_principal, text="Mostrar Nombre", command=mostrar_nombre)
btn_nombre.pack(pady=10)

btn_mensaje = tk.Button(ventana_principal, text="Mostrar Mensaje", command=mostrar_mensaje)
btn_mensaje.pack(pady=10)

# Ejecutar la aplicación
ventana_principal.mainloop()