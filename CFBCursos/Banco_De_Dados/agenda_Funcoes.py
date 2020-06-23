import sqlite3
from sqlite3 import Error


def ConexaoBanco():
    caminho = "//home//lucas//Documentos//GitHub//Python//CFBCursos//Banco_De_Dados//Agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    else:
        print("Conexao realizada com sucesso! ")
    return con



def menuPrincipal():
    print("1 - Inserir Novo Registro ")
    print("2 - Deletar Registro ")
    print("3 - Atualizar Registro ")
    print("4 - Consultar Registro por ID ")
    print("5 - Consultar Resgistro por Nome ")
    print("6 - Sair")


def menuAtualizar():
    print()


def menuConsultarId():
    print()


def menuConsultarNomes():
    print()


def menuDeletar():
    print()


def menuInserir():
    print()
