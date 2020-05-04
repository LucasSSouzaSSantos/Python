"""
EXERCÍCIO 071: Simulador de Caixa Eletrônico
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
"""
while True:
    valor = int(input("Qual o valor do saque: "))
    quantidade50 = valor // 50
    resto50 = valor % 50
    quantidade20 = resto50 // 20
    resto20 = resto50 % 20
    quantidade10 = resto20 // 10
    resto10 = resto20 % 10
    quantidade1 = resto10
    print(f"{quantidade50} x 50 + {quantidade20} x 20 + {quantidade10} x 10 + {quantidade1} x 1")
    opcao = str(input("Desligar: [Ss/Nn]: ")).upper().strip()
    if opcao in 'Ss':
        break
