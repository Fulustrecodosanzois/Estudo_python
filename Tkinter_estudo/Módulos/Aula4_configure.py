# Configure()

# Ao usar o método configure(), substitua "widget" pelo nome do widget que você deseja configurar.

#Por exemplo, se você deseja alterar a cor de fundo (background) de um botão chamado meu_botao. Exemplo: 

#meu_botao.configure(bg="cor")


janela.configure(bg="cor")# Alterar a cor de fundo (background) do widget:

janela.configure(fg="cor")# Alterar a cor do texto (foreground) do widget:

janela.configure(font=("nome_da_fonte", tamanho, "estilo"))# Alterar a fonte do texto do widget:

janela.configure(state="disabled")# Desabilitar um widget:

janela.configure(state="normal")# Habilitar um widget:

janela.configure(borderwidth=valor)# Alterar a largura da borda de um widget:

janela.configure(relief="estilo")# Alterar o estilo da borda de um widget:

janela.configure(spacing2=valor)# Alterar a altura da linha em um widget de texto (Text):

janela.configure(orient="vertical" ou "horizontal")# Alterar a orientação de um widget (vertical ou horizontal):

janela.configure(width=valor)# Alterar a largura da barra de rolagem de um widget:

widget.configure(command=funcao)# Definir um comando (função) a ser executado quando o valor de um widget, como um Slider (Scrollbar) ou uma Caixa de Verificação (Checkbutton), é alterado:
botao.config(command=clicado)

widget.configure(padx=valor, pady=valor)# widget.configure(padx=valor, pady=valor)

widget.configure(justify="left", "center" ou "right")# Alterar o alinhamento horizontal do texto em um widget, como um rótulo (Label) ou botão (Button):

widget.configure(image=imagem)# Alterar a imagem exibida em um widget:

widget.configure(compound="top", "bottom", "left", "right" ou "center")# Alterar a posição da imagem em relação ao texto em um widget:

widget.configure(takefocus=valor)# Alterar a sensibilidade do widget a eventos do mouse:

widget.configure(cursor="nome_do_cursor")# Alterar o estilo do cursor quando o mouse está sobre o widget:

valor_bg = widget.cget("bg")  # Obtém o valor atual da cor de fundo (background)- valor_bg = widget.cget("bg")  # Obtém o valor atual da cor de fundo (background)

#MÉTODO .CONFIGURE()

# Para configurar uma opção específica, você pode passar o nome da opção como argumento para o método .configure() e atribuir um novo valor a ela.
widget.configure(opcao="novo_valor")

# Para configurar várias opções ao mesmo tempo, você pode passar pares de nome de opção e valor como argumentos para o método .configure()
widget.configure(opcao1="valor1", opcao2="valor2", opcao3="valor3")

# Para obter o valor atual de uma opção, você pode chamar o método .configure() sem passar nenhum argumento para ele. Isso retornará um dicionário contendo todas as opções e seus valores atuais.
configuracoes = widget.configure()

#  podem aceitar uma função de retorno de chamada (callback) que será executada quando a opção for alterada. Para isso, você pode passar o nome da opção seguido pela função de retorno de chamada como argumentos para o método .configure()
widget.configure(opcao=funcao_de_retorno)

#Configurar uma opção usando um dicionário:
# Em vez de passar pares de nome de opção e valor como argumentos separados, você também pode passar um dicionário contendo as opções e seus valores para o método .configure()
configuracoes = {"opcao1": "valor1", "opcao2": "valor2", "opcao3": "valor3"}
widget.configure(**configuracoes)

# Configurar uma opção usando o método config:
# Em vez de usar o método .configure(), você também pode usar o método config para configurar uma opção. Esses dois métodos são equivalentes.
widget.config(opcao="novo_valor")

# Configurar uma opção usando o nome da opção como atributo:
# Além de usar o método .configure() ou .config(), você também pode usar o nome da opção como um atributo do widget para configurar seu valor.
widget.opcao = "novo_valor"