"""
EXERCÍCIO 065: Maior e Menor Valores
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""
menor = maior = 0
cont = 0
soma = 0
media = 0
print("".center(40, '-'))
opcao = str(input("Deseja digitar valores[Ss/Nn]: ".ljust(38))).upper().strip()
while opcao not in ['N', 'S']:
    opcao = str(input("Erro: Digite novamente[Ss/Nn]: ".ljust(38))).upper().strip()
while opcao in 'Ss':
    valor = int(input(f"Informe o valor {cont + 1}: "))
    if cont == 0:
        menor = maior = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    soma += valor
    cont += 1
    opcao = str(input("Deseja digitar valores[Ss/Nn]: ".ljust(38))).upper().strip()
    while opcao not in ['N', 'S']:
        opcao = str(input("Erro: Digite novamente[Ss/Nn]: ".ljust(38))).upper().strip()

print("".center(40, '-'))
print("  " + "".center(25, '-'))
print("| " + f"Quantidade: {cont}".ljust(25) + "|")
print("| " + f"Maior: {maior} Menor: {menor}".ljust(25) + "|")
if cont == 0:
    print("| " + "Nenhum número digitado".ljust(25) + "|")
else:
    print("| " + f"Média: {round(soma / cont, 3)}".ljust(25) + "|")
print("  " + "".center(25, '-'))
