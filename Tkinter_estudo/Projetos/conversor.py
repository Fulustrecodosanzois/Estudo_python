import tkinter as tk
from tkinter import ttk

def converter():
    valor = float(entrada.get())
    unidade_origem = combo_origem.get()
    unidade_destino = combo_destino.get()

    if unidade_origem == "Centímetros":
        if unidade_destino == "Metros":
            resultado = valor / 100
        elif unidade_destino == "Polegadas":
            resultado = valor / 2.54
        else:
            resultado = valor
    elif unidade_origem == "Metros":
        if unidade_destino == "Centímetros":
            resultado = valor * 100
        elif unidade_destino == "Polegadas":
            resultado = valor * 39.37
        else:
            resultado = valor
    else:  # Unidade de origem é Polegadas
        if unidade_destino == "Centímetros":
            resultado = valor * 2.54
        elif unidade_destino == "Metros":
            resultado = valor * 0.0254
        else:
            resultado = valor

    saida.config(state="normal")
    saida.delete(0, tk.END)
    saida.insert(tk.END, resultado)
    saida.config(state="readonly")

janela = tk.Tk()
janela.title("Conversor de Unidades")

janela.geometry

lbl_valor = tk.Label(janela, text="Valor:")
lbl_valor.pack()

entrada = tk.Entry(janela)
entrada.pack()

lbl_origem = tk.Label(janela, text="De:")
lbl_origem.pack()

combo_origem = ttk.Combobox(janela, values=["Centímetros", "Metros", "Polegadas"])
combo_origem.pack()

lbl_destino = tk.Label(janela, text="Para:")
lbl_destino.pack()

combo_destino = ttk.Combobox(janela, values=["Centímetros", "Metros", "Polegadas"])
combo_destino.pack()

lbl_resultado = tk.Label(janela, text="Resultado:")
lbl_resultado.pack()

saida = tk.Entry(janela, state="readonly")
saida.pack()

btn_converter = tk.Button(janela, text="Converter", command=converter)
btn_converter.pack()


janela.geometry("200x220")

janela.mainloop()
