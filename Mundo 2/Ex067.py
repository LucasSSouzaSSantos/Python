"""
EXERCÍCIO 067: Tabuada v3.0
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

while True:
    num = int(input("Informe um número: "))
    if num < 0:
        break
    cont = 0
    while cont < 11:
        if num * cont < 10:
            print(f"{num}".ljust(3) + "+".ljust(3) + f"{cont}".ljust(3)
                  + "=".ljust(3) + f"0{num * cont}".rjust(3))
        else:
            print(f"{num}".ljust(3) + "+".ljust(3) + f"{cont}".ljust(3)
                  + "=".ljust(3) + f"{num * cont}".rjust(3))
        cont += 1
