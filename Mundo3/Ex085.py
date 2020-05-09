"""
EXERCÍCIO 085: Listas com Pares e Ímpares
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
crescente.
"""
listaPar = []
listaImpar = []
lista = []
for x in range(0, 7):
    num = int(input(f"Número{x + 1}: "))
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
listaPar.sort()
listaImpar.sort()
lista.append(listaPar)
lista.append(listaImpar)
print(lista)
