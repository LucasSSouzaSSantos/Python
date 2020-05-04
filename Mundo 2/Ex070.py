"""
EXERCÍCIO 070: Estatísticas em Produtos
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""
soma = 0
quantidadeMaisDeMil = 0
precoMaisBarato = 0
nomeProdutoMaisBarato = ""
opcao = str(input("Começar: ")).upper().strip()
while opcao[0] == 'S':
    while True:
        # Aqui é passado o nome e o preço do produto
        nome_produto = str(input("Nome do produto: ")).upper().strip()
        preco = float(input("Preço do produto: "))
        # Aqui verifica quantos produtos tem o preço acima de 1000 reais
        if preco > 1000:
            quantidadeMaisDeMil += 1
        # Aqui verifica o produto mais barato
        if precoMaisBarato == 0:
            precoMaisBarato = preco
        else:
            if preco < precoMaisBarato:
                nomeProdutoMaisBarato += ""
                nomeProdutoMaisBarato = nome_produto
        # Aqui é Somado os Preços dos produtodos
        soma += preco
        # Aqui verifica se o usuário quer permanecer no produto.
        opcao = str(input("Proximo: ")).upper().strip()
        if opcao[0] == 'N':
            break
    # Aqui é imprimido os valores:
    print(f"Preço Total: {soma}.")
    print(f"A quantidade de produtos acima de 1000 R$: {quantidadeMaisDeMil}.")
    print(f"O produto mais barato é: {nomeProdutoMaisBarato}.")
