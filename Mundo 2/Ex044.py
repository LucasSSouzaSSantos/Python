"""
EXERCÍCIO 044: Gerenciador de Pagamentos
Elabore um programa que calcule o valor a ser pago de um produto,
considerando o seu preço normal, e condição de pagamento:
- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
from time import sleep
print(15 * "-=-")
print("OPÇÕES".center(45))
print(15 * "-=-")
print("""1- À vista no dinheiro/cheque: 10% de desconto
2- À vista no cartão: 5% de desconto
3- Em até 2x no cartão: preço normal
4- 3x ou mais no cartão: 20% de juros
5- Desistir da Compra""")
print(15 * "-=-")
opcao = int(input("Opção: "))
sleep(2)
print(15 * "-=-")
sleep(1)

if opcao == 1:
    print("Você escolheu a opção até 2x no cartão \nno cheque ganhando 10% de desconto.\n"
          "Tenha uma boa compra!!!")
    preco = float(input("Informe o valor do Produto: "))
    print(30 * "-")
    sleep(1)
    print(f"Nome do Produto:    X    \n"
          f"Valor do Produto: {preco}\n"
          f"Quantidade de parcelas: A vista\n"
          f"Valor da Total: {preco}")
    sleep(1)
    print("Obrigado e volte sempre!!!")

elif opcao == 2:
    print("Você escolheu a opção á vista no cartão \nganhou 5% de desconto.\n"
          "Tenha uma boa compra!!!")
    preco = float(input("Informe o valor do Produto: "))
    print(30 * "-")
    sleep(1)
    print(f"Nome do Produto:    X    \n"
          f"Valor do Produto: {preco}\n"
          f"Valor com Desconto: {0.5 * preco}"
          f"Quantidade da parcela: A vista no cartão\n"
          f"Valor Total: {preco}")
    sleep(1)
    print("Obrigado e volte sempre!!!")

elif opcao == 3:
    print("Você escolheu a opção de 2x no cartão\nSem Juros.\n"
          "Tenha uma boa compra!!!")
    preco = float(input("Informe o valor do Produto: "))
    print(30 * "-")
    sleep(1)
    print(f"Nome do Produto:    X    \n"
          f"Valor do Produto: {preco}\n"
          f"Quantidade: 2 parcelas\n"
          f"Juros: 0"
          f"Valor da Parcela: {preco / 2}")
    sleep(1)
    print("Obrigado e volte sempre!!!")

elif opcao == 4:
    print("Você escolheu a opção 3x no cartão\nTerá 20% de juros no preço do produto.\n"
          "Tenha uma boa compra!!!")
    preco = float(input("Informe o valor do Produto: "))
    print(30 * "-")
    sleep(1)
    print(f"Nome do Produto:    X    \n"
          f"Valor do Produto: {preco}\n"
          f"Juros: {0.2 * preco}\n"
          f"Quantidade: 3 parcelas\n"
          f"Valor com Desconto: {1.2 * preco}")
    sleep(1)
    print("Obrigado e volte sempre!!!")

elif opcao == 5:
    print("Se o produto não agradou você, você pode escolher outro produto.")

else:
    print("Opção Invalida")
print(15 * "-=-")
