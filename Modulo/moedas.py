def aumentar(preco=0, taxa=0, f=False):
    res = preco + (preco * taxa) / 100
    if f:
        return moeda(res)
    else:
        return f"{res:.2f}"


def diminuir(preco=0, taxa=0, f=False):
    res = preco * (1 - taxa / 100)
    if f:
        return moeda(res)
    else:
        return f"{res:.2f}"


def dobro(preco=0, f=False):
    res = 2 * preco
    if f:
        return moeda(res)
    else:
        return f"{res:.2f}"


def metade(preco=0, f=False):
    res = preco / 2
    if f:
        return moeda(res)
    else:
        return f"{res:.2f}"


def moeda(preco=0, f=False, m='R$'):
    return f"{m}{preco:>8.2f}".replace('.', ',')


def resumo(p, a, d):
    print("".center(30, '-'))
    print(f"RESUMO DE VALOR".center(30, ' '))
    print("".center(30, '-'))
    print(f"Preço analisado: {moeda(p)}")
    print(f"Dobro do preço: {dobro(p, True)}")
    print(f"Metado do preço: {metade(p, True)}")
    print(f"{a}% de aumento: {aumentar(p, a, True)}")
    print(f"{d}% de redução: {diminuir(p, d, True)}")
    print("".center(30, '-'))
