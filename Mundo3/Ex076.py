"""
EXERCÍCIO 076: Lista de Preços com Tupla
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
lista = ('Cerveja importada', 11.70, 'Cerveja nacional', 5.50, 'Garrafa de vinho', 30.00,
	    'Água', 2.95, 'Alface', 2.80, 'Cebola', 3.90, 'Batatas' , 3.90, 'Tomates', 5.60)
print(" Tabela de Preços ".center(70))
print(70 * "-")
for x in range(0, len(lista), 2):
  if lista[x+1] < 10:
    print(f"  {lista[x]} ".ljust(20) + "".center(40, '-') + "R$".rjust(3) + f" 0{round(lista[x + 1], 2)}".ljust(6))
  else:
    print(f"  {lista[x]} ".ljust(20) + "".center(40, '-') + "R$".rjust(3) + f" {round(lista[x + 1], 2)}".ljust(6))
print(70 * "-")
print(" Fim Da Tabela ".center(70))
