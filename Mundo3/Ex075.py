"""
EXERCÍCIO 075: Análise de Dados em uma Tupla
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, 
mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
lista = (int(input("Número: ")), int(input("Número: ")), int(input("Número: ")), int(input("Número: ")))
print(lista)
posicao3 = -1 # O -1 é um valor para indicar que o número 3 não apareceu em nenhuma posição
quant9 = 0
quantPares = 0
for x in range(0,4):
  if lista[x] == 9:
    quant9 += 1
  if lista[x] == 3 and posicao3 == -1:
    posicao3 = x + 1
  if lista[x] % 2 == 0:
    quantPares += 1
print(f"O número 9 apareceu {quant9} vezes.")
if posicao3 == -1:
  print("O número 3 não apareceu em nenhuma posição.")
else:
  print(f"O número 3 apareceu na {posicao3}° posição pela primeira vez.")
print(f"Existe {quantPares} números pares")
