"""
EXERCÍCIO 059: Criando um Menu de Opções
Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
print(" ".center(40, '-'))
valor1 = int(input(" Valor 1: ".center(20)))
valor2 = int(input(" Valor 2: ".center(20)))
print(" ".center(40, '-'))

print("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
""".center(40, '-'))
print(" ".center(40, '-'))
opcao = int(input("Informe a sua OPÇÃO: ".center(20)))
print(" ".center(40, '-'))

while opcao not in [1, 2, 3, 4, 5]:
    opcao = int(input("Erro: Digite novamente! ".center(20)))
    print(" ".center(40, '-'))

while opcao != 5:
    if opcao == 1:
        print("SOMA: ")
        print(f"{valor1} + {valor2} = {valor1 + valor2}")
    if opcao == 2:
        print("MULTIPLICAR: ")
        print(f"{valor1} x {valor2} = {valor1 * valor2}")
    if opcao == 3:
        print("MAIOR: ")
        if valor1 > valor2:
            print(f"{valor1} > {valor2}")
        else:
            print(f"{valor2} > {valor1}")
    if opcao == 4:
        print("MUDAR: ")
        valor1 = int(input("Novo valor1: "))
        valor2 = int(input("Novo valor2: "))
    if opcao == 5:
        print("Sair")

    print(" ".center(40, '-'))
    opcao = int(input("Escolha sua opção: "))
    print(" ".center(40, '-'))
print(" FIM DO PROGRAMA ".center(40, '-'))
