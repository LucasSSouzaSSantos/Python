"""
EXERCÍCIO 077: Contando Vogais em Tupla
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavra = ('casa', 'comida', 'filme', 'mosqueteiro', 'sombra', 'iluminação', 'falso', 'deus', 'igreja',
           'bíblia', 'mandamento', 'versiculos', 'consagração', 'hospital', ' casa grande', 'armario',
           'lupita')
vogais = ('a', 'á', 'à', 'ã', 'e', 'é', 'è', 'i', 'í', 'o', 'ó', 'õ', 'u', 'ú')
print("Palavra  ".center(15) + "".center(40, '-') + " Vogais")
print("")
for x in range(0, len(palavra)):
    print(f"{palavra[x]}  ".center(15) + "".center(40, '-'), end=' ')
    for y in range(0, len(palavra[x])):
        if palavra[x][y] in vogais:
            print(palavra[x][y], end=' ')
    print("\n")
