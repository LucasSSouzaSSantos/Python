"""
EXERCÍCIO 081: Extraindo Dados de uma Lista
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
cont = 0
lista = []
while True:
    num = int(input(f"Número{cont}: "))
    lista.append(num)
    opcao = str(input("Deseja continuar: ")).upper().strip()
    cont += 1
    if opcao == 'N':
        break
print(f"A quantidade de números foi {cont}")
lista.sort(reverse=True)
print(f"Lista na ordem decrescente: {lista}")
if 5 in lista:
    print(f"O valor 5 foi digitado na posição {lista.index(5) + 1}")
else:
    print("O valor 5 não foi digitado")
