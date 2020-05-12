# interactive help
"""
Você pode digitar help() e dentro dos parenteses colocar o nome da funçao e o python vai explicar as funcionalidades
"""
# help(print)
# print(print.__doc__)

# docstrings é uma string de documentação


def contador(i, f, p):
    """
    -> faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    cont = i
    while cont <= f:
        print(f"{cont}", end=' ')
        cont += p
    print("FIM!")


contador(2, 10, 2)
help(contador)
# Argumentos opcionais


def somar(a, b, c=0):
    s = a + b + c
    print(f"A soma vale {s}")


somar(3, 4, 5)
somar(8, 4)
"""
Essa chamada da funçao somar() teria problema, já que só é recebido 2 parâmetros. Contudo, é possivel usar parâmetros 
opçionais; como é demostrado dentro da funçao somar(), o valor do parâmetro c recebe zero se ele nao for informado 
dentro da chamada, como é visto no segundo exemplo.
"""

# Escopo de variáveis
"""
É o local aonde a variável vai existir e o local aonde ela nao vai mais existir
"""


def teste():
    x = 8
    # x tem um escopo local
    print(f"Na funçao teste, n vale {n}")
    print(f"Na funçao teste, x vale {x}")


n = 2
# n tem um escopo global
print(f"No programa principal, n vale {n}")
# print(f"No programa principal, x vale {x}")  essa linha deu erro, pois x estar fora de escopo: ele é local

# Retorno de resultados


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


som = soma(3, 4, 5)
print(f"A soma vale {som}")
