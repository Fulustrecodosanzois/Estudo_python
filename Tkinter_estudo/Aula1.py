import tkinter as tk

janela = tk.Tk() # Tk(): Essa função é usada para criar uma instância da classe Tk, que representa uma janela principal da interface gráfica.

rotulo= tk.Label(janela,text="Click")


# Método iconbitmap()

#O método iconbitmap() em Tkinter permite definir o ícone da janela principal. No entanto, suas possibilidades são um pouco limitadas. O método iconbitmap() aceita apenas um caminho para um arquivo de ícone (.ico) como argumento. Isso significa que você pode fornecer apenas um arquivo de ícone específico para ser usado como o ícone da janela principal.


#iconbitmap(bitmap)= bitmap: Uma string que representa o caminho para o arquivo de ícone (.ico) que você deseja usar como ícone da janela.

janela.iconbitmap("caminho_para_o_arquivo.ico")





rotulo.pack()

janela.mainloop() # É um método que inicia o loop principal do Tkinter, permitindo que a janela seja exibida e interaja com o usuário.


