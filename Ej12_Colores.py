# oscar ivan rueda rodriguez
# 3° programacion T.M:
# cbtis #89
#te da a elegir colores y te da su color

import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista desplegable ComboBox")
ventana.geometry("300x200")

# Etiqueta inicial
etiqueta = tk.Label(ventana, text="Elige una opcion")
etiqueta.pack(pady=10)

# Opciones para el Combobox
opciones = ["Rojo", "Verde", "Azul", "Amarillo", "Morado"]

# Crear Combobox con opciones
ComboColores = ttk.Combobox(ventana, values=opciones, state="readonly")
ComboColores.pack(pady=5)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Selecciona el color")
etiqueta_resultado.pack(pady=20)

# Etiqueta cuyo fondo cambiará de color
Colores = tk.Label(ventana, text=" ")
Colores.pack()

# Función para mostrar la selección y cambiar colores
def mostrar_seleccion(event):
    seleccion = ComboColores.get()  # Obtener la opción seleccionada

    if seleccion == "Rojo":
        Colores.config(bg="red")
        Color = "red"
    elif seleccion == "Verde":
        Colores.config(bg="green")
        Color = "green"
    elif seleccion == "Azul":
        Colores.config(bg="blue")
        Color = "blue"
    elif seleccion == "Amarillo":
        Colores.config(bg="yellow")
        Color = "yellow"
    else:
        Colores.config(bg="purple")
        Color = "purple"

    etiqueta_resultado.config(text=f"Seleccionaste: {seleccion}", fg=Color)

# Asociar el evento de selección del Combobox con la función
ComboColores.bind("<<ComboboxSelected>>", mostrar_seleccion)

# Ejecutar la ventana
ventana.mainloop()
