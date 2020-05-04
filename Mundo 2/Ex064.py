"""
EXERCÍCIO 064: Tratando Vários Valores v1.0
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
foi a soma entre eles (desconsiderando o flag).
"""
cont = 0
print("Digite valores ou digite 999 para acabar")
valor = int(input("Informe o valor: "))
while valor != 999:
    if valor != 999:
        cont += 1
    valor = int(input("Informe o valor: "))
print(f"A quantidade de valores digitado foi {cont}.")


