import tkinter as tk

def button_click():
    label.config(text="O botão foi clicado!")

root = tk.Tk()

label = tk.Label(root, text="Clique no botão!")
label.pack()

button = tk.Button(root, text="Clique aqui", command=button_click)
button.pack()

root.mainloop()
