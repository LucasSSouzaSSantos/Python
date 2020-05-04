"""
EXERCÍCIO 026: Primeira e Última Ocorrência de uma String
Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
"""

string = str(input("Informe o texto:")).upper().strip()

print(f"O caractere 'a' apareceu {string.count('A') + string.count('Á') + string.count('À')} vezes na String. ")
print(f"O caractere 'a' apareceu pela primeira vez na posição {string.find('A') + 1} da String. ")
print(f"O caractere 'a' apareceu pela ultima vez na posição {string.rfind('A') + 1} da String.")

