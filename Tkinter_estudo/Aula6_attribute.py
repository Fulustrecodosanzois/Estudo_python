#MÉTODO .ATTRIBUTES()

# Define a opacidade da janela principal. O valor deve estar entre 0.0 (totalmente transparente) e 1.0 (totalmente opaco). 
janela.attributes("-alpha", 0.8)

# Define se a janela principal deve ser exibida em modo de tela cheia. O valor deve ser True ou False.
janela.attributes("-fullscreen", True)

# Define se a janela principal deve ser exibida no topo de outras janelas. O valor deve ser True ou False. 
janela.attributes("-topmost", True)

# Define se a janela principal deve ser exibida como desabilitada, impedindo interações do usuário. O valor deve ser True ou False. 
janela.attributes("-disabled", True)

# Define se a janela principal deve ser exibida como uma janela de ferramentas, geralmente com uma aparência mais compacta. O valor deve ser True ou False. 
janela.attributes("-toolwindow", True)

# Define uma cor específica para ser tratada como transparente na janela principal. Você precisa especificar a cor em formato hexadecimal, por exemplo, "#RRGGBB". 
janela.attributes("-transparentcolor", "#FFFFFF")

# Define o estado modificado da janela principal. O valor deve ser True ou False.
janela.attributes("-modified", True)

# Define as decorações da janela, como barras de título e bordas. O valor deve ser uma string que define o estilo das decorações.
janela.attributes("-decorations", "none")

# Define o tipo da janela. O valor deve ser uma string que define o tipo, como "dialog" (caixa de diálogo) ou "splash" (tela de apresentação). 
janela.attributes("-type", "dialog")

# Define se a janela principal deve ser exibida como transparente. O valor deve ser True ou False.
janela.attributes("-transparent", True)

# Define se a janela principal deve ser exibida em modo de tela cheia maximizada. O valor deve ser True ou False.
janela.attributes("-zoomed", True)

# Define se a janela principal deve ser exibida no topo de outras janelas. O valor deve ser True ou False.
janela.attributes("-topmost", True)

# Define a posição inicial da janela principal na tela, especificando o valor y (vertical) em pixels
janela.attributes("-top", 100)

# Define a posição inicial da janela principal na tela, especificando o valor x (horizontal) em pixels. 
janela.attributes("-left", 200)