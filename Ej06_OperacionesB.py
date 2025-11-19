# oscar ivan rueda rodriguez
# 3° programacion T.M:
# cbtis #89
#da resultados de sumas basicas

import tkinter as tk
from tkinter import messagebox

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"resultadov: {num1 + num2}")
    except ValueError:
        messagebox.showerror("error ", "por favor ingresa solo numeros")

def restar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"resultado: {num1 - num2}")
    except ValueError:
        messagebox.showerror("error", "por favor ingresa solo numeros")

def multiplicar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"rtesultado: {num1 * num2}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números")

def dividir():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        if num2 == 0:
            messagebox.showerror("Error", "No se puede dividir entre cero")
        else:
            resultado.config(text=f"Resultado: {num1 / num2}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa solo números")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("350x280")

# Etiquetas y entradas
tk.Label(ventana, text="Número 1:").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)

tk.Label(ventana, text="Número 2:").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

# Botones de operaciones
tk.Button(ventana, text="Sumar", command=sumar).pack(pady=5)
tk.Button(ventana, text="Restar", command=restar).pack(pady=5)
tk.Button(ventana, text="Multiplicar", command=multiplicar).pack(pady=5)
tk.Button(ventana, text="Dividir", command=dividir).pack(pady=5)

# Etiqueta del resultado
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()