"""
EXERCÍCIO 066: Vários Números com Flag
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
cont = 0
print("Digite valores ou digite 999 para acabar")
while True:
    valor = int(input("Informe o valor: "))
    if valor == 999:
        break
    cont += 1
print(f"A quantidade de valores digitado foi {cont}.")
