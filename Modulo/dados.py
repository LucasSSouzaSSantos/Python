from modulos.moedas import resumo


def leiaDinheiro(msg):
    valido = False
    while not valido:
        num = str(input(" ")).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print("Erro: Digite novamente: ")
        else:
            resumo(num, 80, 35)
            valido = True
