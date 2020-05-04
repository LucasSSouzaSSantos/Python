"""
EXERCÍCIO 043: Índice de Massa Corporal
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

peso = float(input("Informe seu Peso: "))
altura = float(input("Informe sua altura: "))
IMC = peso / pow(altura, 2)

print(15 * "-=-")
print(f"Peso: {peso} Altura: {altura}".center(45))
if IMC < 18.5:
    print(f"IMC: {round(IMC, 2)} Situação: Abaixo do Peso".center(45))
elif 18.5 <= IMC < 25:
    print(f"IMC: {round(IMC, 2)} Situação: Peso Ideal".center(45))
elif 25 <= IMC < 30:
    print(f"IMC: {round(IMC, 2)} Situação: SobrePeso".center(45))
elif 30 <= IMC < 40:
    print(f"IMC: {round(IMC, 2)} Situação: Obesidade".center(45))
else:
    print(f"IMC: {round(IMC, 2)} Situação: Obesidade Morbida".center(45))
print(15 * "-=-")
