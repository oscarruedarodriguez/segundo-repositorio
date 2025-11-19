# oscar ivan rueda rodriguez
# 3° programacion T.M:
# cbtis #89
#pide una contraseña para acceder

import tkinter as tk
from tkinter import messagebox

# Función para verificar la contraseña
def verificar_password():
   password = entrada_password.get()
   if password == "12345":
      messagebox.showinfo("Resultado", "Acceso correcto")
   else:
      messagebox.showwarning("Resultado", "Acceso denegado")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Verificador de acceso")
ventana.geometry("300x150")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingresa la contraseña:")
etiqueta.pack(pady=10)

# Cuadro de texto (password)
entrada_password = tk.Entry(ventana, show="*")
entrada_password.pack()

# Botón
boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_password)
boton_verificar.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Función para verificar la contraseña
def verificar_password():
   password = entrada_password.get()
   if password == "12345":
      messagebox.showinfo("Acceso", "Acceso correcto")
   else:
      messagebox.showerror("Acceso", "Acceso denegado")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Acceso")
ventana.geometry("350x200")
ventana.configure(bg="#f0f4f8") # color de fondo claro

# Fuente personalizada
fuente_titulo = font.Font(family="Helvetica", size=14, weight="bold")
fuente_normal = font.Font(family="Helvetica", size=10)

# Marco centrado
marco = tk.Frame(ventana, bg="#ffffff", bd=2, relief="groove")
marco.place(relx=0.5, rely=0.5, anchor="center")

# Etiqueta de título
titulo = tk.Label(marco, text="Ingrese su contraseña", font=fuente_titulo, bg="#ffffff")
titulo.pack(padx=20, pady=(15, 5))

# Campo de entrada de password
entrada_password = tk.Entry(marco, show="*", font=fuente_normal, width=25, bd=2, relief="solid")
entrada_password.pack(pady=5, padx=20)

# Botón de verificación
boton_verificar = tk.Button(
marco, text="Verificar acceso", command=verificar_password,
bg="#4CAF50", fg="white", font=fuente_normal, padx=10, pady=5,
activebackground="#45a049", relief="flat"
)
boton_verificar.pack(pady=(10, 15))

# Ejecutar la app
ventana.mainloop()