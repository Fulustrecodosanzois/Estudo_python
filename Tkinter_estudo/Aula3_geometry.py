# AJUSTE DA JANELA

janela.geometry("500x300") # dimensões da janela especificando a largura e a altura em pixels

janela.geometry("+600+340") #a posição da janela especificando a largura, altura e as coordenadas x e y da janela

janela.geometry("80%x80%")#Isso permite que a janela se ajuste automaticamente a diferentes tamanhos de tela

largura = 500
altura = 300
x = (janela.winfo_screenwidth() - largura) // 2
y = (janela.winfo_screenheight() - altura) // 2
janela.geometry(f"{largura}x{altura}+{x}+{y}")#Para centralizar a janela na tela, você pode usar o método winfo_screenwidth() e winfo_screenheight() para obter as dimensões da tela e, em seguida, calcular as coordenadas x e y da janela centralizada