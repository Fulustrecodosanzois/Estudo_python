import os

while True:
    pala=input("Digite uma palavra: ")

    total= len(pala)

    if total > 5:
        print("A palavra tem mais de 5 letras")
    elif total < 5:
        print("A palavra tem menos de 5 letras")
    