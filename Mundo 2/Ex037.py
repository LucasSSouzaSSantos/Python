"""
EXERCÍCIO 037: Conversor de Bases Numéricas
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
"""
print("""
1 - Binário
2 - Octal
3 - Hexadecimal
""")
numero = int(input("Informe o Número: "))
opcao = int(input("Opção: "))

lista = []
if opcao == 1:
    while True:
        quociente = numero // 2
        resto = numero % 2
        lista.append(resto)
        numero = quociente
        if numero == 0:
            break
    lista.reverse()

    contador = 0

    while True:
        print(lista[contador], end=' ')
        contador += 1
        if contador == len(lista):
            break

if opcao == 2:
    while True:
        quociente = numero // 8
        resto = numero % 8
        lista.append(resto)
        numero = quociente
        if numero == 0:
            break
    lista.reverse()

    contador = 0

    while True:
        print(lista[contador], end=' ')
        contador += 1
        if contador == len(lista):
            break

if opcao == 3:
    while True:
        quociente = numero // 16
        resto = numero % 16
        lista.append(resto)
        numero = quociente
        if numero == 0:
            break
    lista.reverse()

    contador = 0

    while True:
        print(lista[contador], end=' ')
        contador += 1
        if contador == len(lista):
            break
print("Muito obrigado e volte sempre")
