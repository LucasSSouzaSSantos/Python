"""
EXERCÍCIO 052: Números Primos
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
print(" ".center(40, '-'))
num = int(input("Digite o número: "))
contador = 0
print(" ".center(40, '-'))
print(f"Por definição os números primo tem 2\n"
      f"divisores naturais que são:\n"
      f"ele mesmo, no caso {num}, e o número 1.")
print(" ".center(40, '-'))

for x in range(1, num + 1):
    if num % x == 0:
        contador += 1
if num == 1 or num == 0:
    print(f"Pela definição o número {num} não é um número Primo;\n"
          f"Já que ele só tem um divisor que é ele mesmo.")
else:
    if contador == 2:
        print(f"O número {num} é PRIMO.")
    else:
        print(f"O número {num} não é PRIMO")
