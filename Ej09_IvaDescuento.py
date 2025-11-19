# oscar ivan rueda rodriguez
# 3° programacion T.M:
# cbtis #89
#calcula iva,descuento y te da el resultado


import tkinter as tk
from tkinter import messagebox

# Función para calcular el IVA (Impuesto al Valor Agregado 16%)
def calcular_iva():
    try:
        cantidad = float(entrada_cantidad.get())
        iva = cantidad * 0.16
        etiqueta_resultado.config(text=f"IVA (16%): ${iva:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad válida.")

# Función para calcular el 10% de descuento
def calcular_descuento():
    try:
        cantidad = float(entrada_cantidad.get())
        descuento = cantidad * 0.10
        etiqueta_resultado.config(text=f"Descuento (10%): ${descuento:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad válida.")

# Función para calcular el total a pagar (considerando IVA y descuento)
def calcular_total():
    try:
        cantidad = float(entrada_cantidad.get())
        iva = cantidad * 0.16
        descuento = cantidad * 0.10
        total = cantidad + iva - descuento
        etiqueta_resultado.config(text=f"Total a pagar: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa una cantidad válida.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de IVA y Descuento")
ventana.geometry("350x200")
ventana.resizable(False, False)

# Etiqueta y caja de texto para ingresar la cantidad
etiqueta_cantidad = tk.Label(ventana, text="Ingresa la cantidad:")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad = tk.Entry(ventana, width=20)
entrada_cantidad.pack()

# Botones para calcular IVA, descuento y total
boton_iva = tk.Button(ventana, text="Calcular IVA (16%)", command=calcular_iva, bg="blue", fg="white")
boton_iva.pack(pady=5)

boton_descuento = tk.Button(ventana, text="Calcular Descuento (10%)", command=calcular_descuento, bg="green", fg="white")
boton_descuento.pack(pady=5)

boton_total = tk.Button(ventana, text="Calcular Total a Pagar", command=calcular_total, bg="purple", fg="white")
boton_total.pack(pady=5)

# Etiqueta para mostrar resultados
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
etiqueta_resultado.pack(pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()