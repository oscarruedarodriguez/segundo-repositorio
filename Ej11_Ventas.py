# oscar ivan rueda rodriguez
# 3° programacion T.M:
# cbtis #89
#calcual el iva y total de varios articulos

import tkinter as tk
from tkinter import messagebox

def calcular_iva():
    try:
        cantidad = float(entrada_cantidad.get())
        precio = float(entrada_precio.get())
        iva = (cantidad * precio) * 0.16
        etiqueta_resultado.config(text=f"IVA: ${iva:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

def calcular_subtotal():
    try:
        cantidad = float(entrada_cantidad.get())
        precio = float(entrada_precio.get())
        subtotal = cantidad * precio
        etiqueta_resultado.config(text=f"Subtotal: ${subtotal:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

def calcular_total():
    try:
        cantidad = float(entrada_cantidad.get())
        precio = float(entrada_precio.get())
        subtotal = cantidad * precio
        iva = subtotal * 0.16
        total = subtotal + iva
        etiqueta_resultado.config(text=f"Total: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

ventana = tk.Tk()
ventana.title("Cálculo de ventas")
ventana.geometry("400x350")
ventana.resizable(False, False)

# Etiquetas y cajas de texto
etiqueta_cantidad = tk.Label(ventana, text="Cantidad de artículos")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad = tk.Entry(ventana, justify="center")
entrada_cantidad.pack(pady=5)

etiqueta_precio = tk.Label(ventana, text="Precio por artículo")
etiqueta_precio.pack(pady=5)

entrada_precio = tk.Entry(ventana, justify="center")
entrada_precio.pack(pady=10)

# Botones
boton_subtotal = tk.Button(ventana, text="Calcular subtotal", command=calcular_subtotal)
boton_subtotal.pack(pady=5)

boton_iva = tk.Button(ventana, text="Calcular IVA (16%)", command=calcular_iva, bg="#E2DCD6")
boton_iva.pack(pady=5)

boton_total = tk.Button(ventana, text="Calcular total de la compra", command=calcular_total, bg="#C7D3D4")
boton_total.pack(pady=5)

# Etiqueta para mostrar resultados
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()