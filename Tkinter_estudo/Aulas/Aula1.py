from tkinter import Tk, Button, Label

# Função de ação do botão
def clique():
    print("deu certo")
#cria- se uma função que irá executar a ação do botão.

janela= Tk()
janela.title("Meu app")
janela.geometry("400x200")

# Criação de um botão
botao= Button(janela, text="Click", command=clique)
botao2= Button(janela, text="Click", command=clique)
botao_grid= Button(janela, text="Click", command=clique)

#posicionando o botão em local específico
botao.grid(column=0, row=0, columnspan=2, sticky="nsew", padx=5, pady=5)
# -row= Define a linha na qual o widget deve ser colocado.
# -columnspan= Especifica quantas colunas o widget deve ocupar.
# -sticky= Define como o widget deve se expandir para preencher o espaço alocado. Pode ser usado para definir a ancoragem nos pontos cardeais (norte, sul, leste, oeste) ou combinações desses pontos.
# -padx= Define o preenchimento horizontal (espaço em branco) em pixels em ambos os lados do widget.
# -pady= Define o preenchimento vertical (espaço em branco) em pixels acima e abaixo do widget.

botao2.grid(column=2, row=0, rowspan=2, sticky="w", padx=10, pady=10)
# -rowspan= Especifica quantas linhas o widget deve ocupar.

botao_grid.grid(column=0, row=1, sticky="e", ipadx=10, ipady=10)
# -ipadx= Define o preenchimento interno horizontal (espaço em branco) em pixels.
# -ipady= Define o preenchimento interno vertical (espaço em branco) em pixels.

botao_grid.grid()

# Adição do botão à janela raiz
# botao.pack()
# botao2.pack()
# botao3.pack()
#.pack() serve para adicionar o botão ou recurso a janela.

#rotulo= Label(janela, text="deu certo")
# Adição do rótulo à janela raiz
# rotulo.pack()

janela.mainloop()