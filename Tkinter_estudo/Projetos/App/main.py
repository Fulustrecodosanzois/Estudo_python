from tkinter import Tk, Listbox, Entry, Button, messagebox, font, Menu, Scrollbar, ttk
import ttkthemes as ttk_themes
import pickle

janela= Tk()

janela.title("Lista de Tarefas")
janela.geometry("340x350")
janela.configure(bg="green")
janela.configure(relief="sunken")
janela.configure()

style = ttk_themes.ThemedStyle(janela)
style.set_theme("arc")

def alterar_estilo_fonte():
    estilo_fonte = font.Font( font="Arial", weight="bold", slant="italic", size=50)
    tarefas_lista.configure(font=estilo_fonte)

def excluir_tarefa():
    selecao = tarefas_lista.curselection()
    if selecao:
        tarefas_lista.delete(selecao)
        
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        tarefas_lista.insert("end", tarefa)
        entrada_tarefa.delete(0, "end")
    else:
        messagebox.showwarning("Aviso", "Insira uma tarefa antes de adicionar.")

def salvar_tarefas():
    tarefas = list(tarefas_lista.get(0, "end"))  # Convertendo as tarefas para uma lista
    with open("tarefas.pkl", "wb") as arquivo:
        pickle.dump(tarefas, arquivo)


tarefas_lista= Listbox(janela, width=50)
tarefas_lista.pack()

entrada_tarefa=Entry(janela, width=50)
entrada_tarefa.pack()

def salvar_tarefas():
    tarefas = list(tarefas_lista.get(0, "end"))  # Convertendo as tarefas para uma lista
    with open("tarefas.pkl", "wb") as arquivo:
        pickle.dump(tarefas, arquivo)

botao_adicionar = ttk.Button(janela, text="Adicionar", command=adicionar_tarefa, style="TButton")
botao_adicionar.pack(pady=5)

botao_excluir = Button(janela, text="Excluir", command=excluir_tarefa)
botao_excluir.pack(pady=5)

botao_fonte= Button(janela, text="Alterar fonte", command=alterar_estilo_fonte)
botao_fonte.pack(pady=5)

estilo_botao = ttk.Style()
estilo_botao.configure("TButton", padding=6, relief="flat")

botao_salvar= Button(janela, text="Salvar", command=salvar_tarefas)
botao_salvar.pack()

menu= Menu(janela)
janela.configure(menu=menu)

menu_opcao= Menu(menu, tearoff=False)
menu.add_cascade(label="Opções", menu=menu_opcao)
menu_opcao.add_command(label="alterar Fonte", command=alterar_estilo_fonte)
menu_opcao.add_command(label="Adicionar", command=adicionar_tarefa)
menu_opcao.add_command(label="Deletar", command=excluir_tarefa)

janela.mainloop()