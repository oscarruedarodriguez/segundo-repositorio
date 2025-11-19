# oscar ivan rueda rodriguez
# 3° programacion T.M:
# cbtis #89
#te da a eleguir una carrera

import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Lista desplegable con botones")
ventana.geometry("350x250")

etiqueta = tk.Label(ventana, text="Elige una opción")
etiqueta.pack(pady=10)

opciones = [
    "ARH",
    "Arquitectura",
    "Comercio electrónico",
    "Comercio internacional",
    "Construcción",
    "Mecatrónica",
    "Programación"
]

ComboCarreras = ttk.Combobox(ventana, values=opciones, state="readonly")
ComboCarreras.pack(pady=5)

def mostrar_seleccion(event):
    seleccion = ComboCarreras.get()
    etiqueta_resultado.config(text=f"Seleccionaste: {seleccion}")

ComboCarreras.bind("<<ComboboxSelected>>", mostrar_seleccion)

etiqueta_resultado = tk.Label(ventana, text="Selecciona una carrera")
etiqueta_resultado.pack(pady=20)

ventana.mainloop()
