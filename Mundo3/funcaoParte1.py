def MostraLinhas():  # Toda função em python é identificado pelo abrir e fechar de parenteses
    print(40 * "-")


def escreve(msg):
    print(f" {msg} ".center(40))
    MostraLinhas()


def soma(a, b):
    print(f"a + b = {a + b}".center(40))


def contador(* num):
    print(f"{num}".center(40))


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(f"{lst}".center(40))


MostraLinhas()
escreve('Sistema de Alunos')
escreve('Cadastrado de Funcionários')
escreve('Erro do Sistema')
escreve('soma')
soma(4, 5)
soma(5, 89)
soma(3, 6)
MostraLinhas()
escreve('Compactador')
contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
MostraLinhas()
escreve('Dobra Valores')
dobra([6, 3, 9, 1, 0, 2])
MostraLinhas()
