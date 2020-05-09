"""
EXERCÍCIO 082: Dividindo Valores em Várias Listas
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, cria duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
três listas geradas.
"""
lista = []
cont = 0
while True:
    num = int(input(f"Número{cont + 1}: "))
    lista.append(num)
    cont += 1
    opcao = str(input("Deseja continuar: ")).upper().strip()
    if opcao == 'N':
        break
print(f"Lista = {lista}")
listaPar = []
listaImpar = []
for c in lista:
    if c % 2 == 0:
        listaPar.append(c)
    else:
        listaImpar.append(c)
print(f"Valores Pares = {listaPar}")
print(f"Valores Impares = {listaImpar}")
