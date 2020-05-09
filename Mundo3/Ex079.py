"""
EXERCÍCIO 079: Valores Únicos em uma Lista
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""
lista = []
while True:
    num = int(input("Digite um valor: "))
    if len(lista) == 0:
        print("Número novo vou adicionar")
        lista.append(num)
    else:
        if num in lista:
            print("Não vou adicionar")
        else:
            print("Número novo vou adicionar")
            lista.append(num)
    if len(lista) == 5:
        break
print(lista)
