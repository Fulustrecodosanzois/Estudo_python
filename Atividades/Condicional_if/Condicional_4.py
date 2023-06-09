while True:

    entrada=input("Digite algo: ")

    resul= entrada.isdigit()
    resul2= entrada.isalpha()

    if resul == False:
        print("não há números")
        
    if resul2 == False:
        print("não há letras")

