"""
EXERCÍCIO 080: Lista Ordenada sem Repetições
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
maior = menor = 0
lista = []
for x in range(0, 5):
    num = int(input(f"Número {x + 1}: "))
    if x == 0:
        print(f"{num} será adicionado na {x + 1}º")
        lista.append(num)
        maior = menor = num
    else:
        if num >= maior:
            maior = num
            print(f"{num} será adicinionado na 5º posição")
            lista.append(num)
        elif num <= menor:
            menor = num
            print(f"{num} será adicionado na 1º")
            lista.insert(0, num)
        elif menor < num < maior:
            for y in range(1, len(lista) - 1):
                if num <= lista[y]:
                    print(f"{num} será adicionado na posição {y + 1}")
                    lista.insert(y, num)
                    break
print(f"Lista = {lista}")
