# oscar ivan rueda rodriguez
# 3° programacion T.M:
# cbtis #89
#calcular pago dew aguinaldo y bonos de cliente

import tkinter as tk
from tkinter import messagebox

def calcular_sueldo():
    try:
        nombre = entry_nombre.get().strip()
        sueldo_mensual = float(entry_sueldo.get())
        meses_trabajados = int(entry_meses.get())
        if meses_trabajados < 0 or meses_trabajados > 12:
            messagebox.showerror("Error", "meses trabajados debe estar entre 0 y 12")
            return
        tipo_bono = bono_var.get()

        sueldo_por_meses = sueldo_mensual * meses_trabajados
        if meses_trabajados > 3:
            aguinaldo = (sueldo_mensual / 30) * 15  
        else:
            aguinaldo = 0.0
        subtotal = sueldo_por_meses + aguinaldo

        if tipo_bono == "completo":
            porcentaje_bono = 0.10
        elif tipo_bono == "parcial":
            porcentaje_bono = 0.05
        else:
            porcentaje_bono = 0.0

        bono_anual = subtotal * porcentaje_bono
        sueldo_total = subtotal + bono_anual

        resultado = f"""trabajador: {nombre}
sueldo por meses: ${sueldo_por_meses:,.2f}
aguinaldo: ${aguinaldo:,.2f}
subtotal: ${subtotal:,.2f}
bono anual ({tipo_bono}): ${bono_anual:,.2f}
sueldo TOTAL anual: ${sueldo_total:,.2f}"""

        text_resultado.config(state='normal')
        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, resultado)
        text_resultado.config(state='disabled')

    except ValueError:
        messagebox.showerror("error", "por favor ingresa valores numericos validos.")

ventana = tk.Tk()
ventana.title("calculo de sueldo total anual")
ventana.geometry("500x550")


tk.Label(ventana, text="nombre del trabajador:").pack(pady=5)
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.pack()

tk.Label(ventana, text="sueldo mensual:").pack(pady=5)
entry_sueldo = tk.Entry(ventana, width=20)
entry_sueldo.pack()

tk.Label(ventana, text="meses trabajados (0-12):").pack(pady=5)
entry_meses = tk.Entry(ventana, width=20)
entry_meses.pack()

tk.Label(ventana, text="seleccione tipo de bono anual:").pack(pady=5)
bono_var = tk.StringVar(value="completo")

frame_bonos = tk.Frame(ventana)
frame_bonos.pack()

tk.Radiobutton(frame_bonos, text="completo (10%)", variable=bono_var, value="completo").pack(anchor="w")
tk.Radiobutton(frame_bonos, text="parcial (5%)", variable=bono_var, value="parcial").pack(anchor="w")
tk.Radiobutton(frame_bonos, text="sin bono (0%)", variable=bono_var, value="sin bono").pack(anchor="w")

btn_calcular = tk.Button(ventana, text="calcular Sueldo Total", command=calcular_sueldo)
btn_calcular.pack(pady=15)

text_resultado = tk.Text(ventana, height=15, width=60, state='disabled')
text_resultado.pack(pady=10)

ventana.mainloop()