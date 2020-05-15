def aumentar(preco=0, taxa=0):
    return preco + (preco * taxa) / 100


def diminuir(preco=0, taxa=0):
    return preco - (preco * taxa) / 100


def dobro(preco=0):
    return 2 * preco


def metade(preco=0):
    return preco / 2


def moeda(preco=0, m='R$'):
    return f"{m} {preco:.2f}".replace('.', ',')
