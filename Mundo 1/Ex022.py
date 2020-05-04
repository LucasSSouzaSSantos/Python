"""
EXERCÍCIO 022: Analisador de Textos
Crie um programa que leia o nome completo de uma pessoa e mostre:
> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
"""
print("-=-" * 20)
nome = str(input("Digite o seu nome completo: "))
print(f"Seu nome com todas as letras maiúsculas: \n{nome.upper()}")
print(f"Seu nome com todas as letras minúsculas: \n{nome.lower()}")
tamanhoNome = len(nome) - nome.count(' ')
print(f"Seu nome tem o tamanho de {tamanhoNome} caracteres.")
tamanhoPrimeiroNome = len(nome.split()[0])
print(f"Seu primeiro nome tem o tamanho de {tamanhoPrimeiroNome} caracteres.")
print("-=-" * 20)
