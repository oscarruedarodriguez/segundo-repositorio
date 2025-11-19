# oscar ivan rueda rodriguez
# 3° programacion T.M:
# cbtis #89
#te da a eleguir varios descuentos

import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calcular Descuentos")
ventana.geometry("480x600")
ventana.resizable(False, False)  # Evita que el usuario cambie el tamaño de la ventana

# Etiqueta y caja de texto
etiqueta_cantidad = tk.Label(ventana, text="Ingresa la cantidad:")
etiqueta_cantidad.pack(pady=10)

entrada_cantidad = tk.Entry(ventana, justify="center")
entrada_cantidad.pack()

# Variable para la selección del descuento
seleccion = tk.IntVar()
seleccion.set(1)  # Valor por defecto

# Crear botones de radio para seleccionar el porcentaje de descuento
radio_5 = tk.Radiobutton(ventana, text="Descuento 5%", variable=seleccion, value=1)
radio_5.pack()

radio_10 = tk.Radiobutton(ventana, text="Descuento 10%", variable=seleccion, value=2)
radio_10.pack()

radio_15 = tk.Radiobutton(ventana, text="Descuento 15%", variable=seleccion, value=3)
radio_15.pack()

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=20)

# Función que se ejecuta al presionar el botón
def ejecutar_radio():
    try:
        cantidad = float(entrada_cantidad.get())
        opcion = seleccion.get()
        if opcion == 1:
            descuento = cantidad * 0.05
            porcentaje = 5
        elif opcion == 2:
            descuento = cantidad * 0.10
            porcentaje = 10
        elif opcion == 3:
            descuento = cantidad * 0.15
            porcentaje = 15
        else:
            descuento = 0
            porcentaje = 0

        total = cantidad - descuento
        etiqueta_resultado.config(text=f"Hola estimado cliente, usted obtuvo un descuento del {porcentaje}%. "
                                       f"El total a pagar es: ${total:.2f}")
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingrese un número válido.")

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular descuento", command=ejecutar_radio)
boton_calcular.pack()

# Ejecutar la ventana
ventana.mainloop()







#tk.Radiobutton(ventana, text ="bono del 5%")