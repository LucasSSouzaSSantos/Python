"""
EXERCÍCIO 036: Aprovando Empréstimo
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""
valor_casa = float(input("Informe o valor da Casa: "))
valor_salario = float(input("Informe o seu salário: "))
tempo = int(input("Quantidade de Parcelas: "))
condicao = valor_salario * 0.3
parcelas = valor_casa / pow(1.08, tempo)

if round(parcelas) > condicao:
    print(f"15% do salario = {round(condicao)} parcelas = {round(parcelas, 3)}")
    print("O valor da casa foi aceito.")
else:
    print(f"15% do salario = {round(condicao)} parcelas = {round(parcelas, 3)}")
    print("O valor naõ foi aceito.")
