"""
EXERCÍCIO 060: Cálculo do Fatorial
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""
numero = int(input("Fatorial: "))
fatorial = 1
cont = 1
if numero == 0 or numero ==1:
    if numero == 1:
        print(f"1! = 1")
    else:
        print(f"0! = 1")
else:
    while cont <= numero:
        fatorial *= cont
        cont += 1
    print(f"{numero}! = {fatorial}")
